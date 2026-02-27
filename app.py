from flask import Flask, render_template, request, session, current_app
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
from config.settings import Config
from models import db, User
from dotenv import load_dotenv
import os
from datetime import datetime
from sqlalchemy.exc import OperationalError

load_dotenv()

def create_upload_directories(app):
    """
    Ensure that upload directories exist to prevent 500 errors.
    """
    upload_folder = app.config.get('UPLOAD_FOLDER')
    if not upload_folder:
        return

    directories = [
        upload_folder,
        os.path.join(upload_folder, 'logos'),
        os.path.join(upload_folder, 'resumes'),
        os.path.join(upload_folder, 'pitch_decks')
    ]

    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
        except Exception as e:
            # Using print here as logger might not be fully configured or to ensure stdout visibility
            print(f"Error creating directory {directory}: {e}")

class MockSiteSettings:
    header_logo = None
    footer_logo = None
    favicon = None
    site_title = "Shabaka InnovLab"
    privacy_policy = None
    terms_conditions = None
    address = "Marrakech, Maroc"
    phone = "+212 600 00 00 00"
    contact_email = "contact@shabaka.com"
    custom_head_code = None
    telegram_bot_token = None
    telegram_chat_id = None
    linkedin_url = None
    twitter_url = None
    facebook_url = None
    map_latitude = '31.6295'
    map_longitude = '-8.0063'
    notify_on_visit = False
    last_telegram_greeting_date = None

class MockSeoSettings:
    meta_title_default = "Shabaka InnovLab"
    meta_description_default = "Le Catalyseur de la Souveraineté Technologique"
    meta_keywords_default = "innovation, startup, investissement, afrique, technologie"
    og_site_name = "Shabaka InnovLab"
    og_image_default = "/img/logo.png"
    twitter_handle = "@ShabakaInnov"
    google_analytics_id = None
    robots_txt_content = "User-agent: *\nDisallow:"

    # Page specific fields (defaults empty)
    title_tag = None
    meta_desc = None
    keywords = None

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='statics')
    app.config.from_object(Config)

    # Security Configuration
    csrf = CSRFProtect(app)
    # Enable HTTPS force only if not in debug mode
    # NOTE: Force HTTPS set to False for tests to avoid 302 redirects
    # When testing locally with pytest, we need to ensure force_https is False
    # Use environment variable to detect testing if app.config doesn't have it yet
    is_testing = app.testing or app.config.get('TESTING', False) or os.environ.get('FLASK_TESTING') == 'True'
    force_https = not app.debug and not is_testing
    Talisman(app, content_security_policy=None, force_https=force_https)

    limiter = Limiter(
        key_func=get_remote_address,
        app=app,
        default_limits=["200 per day", "50 per hour"],
        storage_uri="memory://"
    )

    # Ensure upload directories exist (Anti-Crash 500)
    create_upload_directories(app)

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from security.auth import load_user
    login_manager.user_loader(load_user)

    # Import and register blueprints/routes
    from routes.public.navigation import main_bp
    app.register_blueprint(main_bp)

    from routes.public.forms import forms_bp
    # Apply stricter limits to forms
    limiter.limit("5 per minute")(forms_bp)
    app.register_blueprint(forms_bp)

    from routes.admin.auth import auth_bp
    app.register_blueprint(auth_bp)

    from routes.admin.dashboard import admin_bp
    app.register_blueprint(admin_bp)

    from routes.admin.portfolio import portfolio_bp
    app.register_blueprint(portfolio_bp)

    from routes.admin.settings import settings_bp
    app.register_blueprint(settings_bp)

    from routes.admin.testimonials import testimonials_admin_bp
    app.register_blueprint(testimonials_admin_bp)

    from routes.api.telegram import telegram_bp
    csrf.exempt(telegram_bp) # Webhook needs to be exempt from CSRF
    app.register_blueprint(telegram_bp, url_prefix='/api/telegram')

    from models.settings import SiteSettings, SeoSettings
    from models.security_logs import BannedIP
    from models.analytics import VisitAnalytics
    from services.notification_service import notify_visit
    from flask import abort
    from flask_login import current_user
    from user_agents import parse
    from utils.i18n import get_locale, setup_i18n

    # Set up i18n
    setup_i18n(app)

    @app.before_request
    def handle_language():
        # Call get_locale to ensure session gets updated on every request
        # if there's a lang parameter
        get_locale()

    # 1. Banned IP Middleware
    @app.before_request
    def block_banned_ips():
        try:
            ip = request.remote_addr
            if ip and BannedIP.query.filter_by(ip_address=ip).first():
                abort(403)
        except OperationalError:
            # Database might not be ready
            pass

    # 2. Analytics Tracking Middleware
    @app.before_request
    def track_visitor():
        try:
            # Ignorer les requêtes statiques et l'admin pour ne pas polluer les stats
            if request.path.startswith('/static') or request.path.startswith('/admin'):
                return

            ip = request.remote_addr
            user_agent_string = request.headers.get('User-Agent', '')
            user_agent = parse(user_agent_string)
            device_type = 'mobile' if user_agent.is_mobile else ('tablet' if user_agent.is_tablet else 'desktop')

            # Vérifier si on a déjà enregistré cette IP pour ce chemin dans les 5 dernières minutes (éviter le spam)
            recent_visit = VisitAnalytics.query.filter_by(ip_address=ip, path=request.path).order_by(VisitAnalytics.timestamp.desc()).first()
            if not recent_visit or (datetime.utcnow() - recent_visit.timestamp).total_seconds() > 300:
                visit = VisitAnalytics(
                    ip_address=ip,
                    user_agent=user_agent.browser.family,
                    path=request.path,
                    referrer=request.referrer,
                    device_type=device_type
                )
                db.session.add(visit)
                db.session.commit()

                # Optionnel : Notification Telegram
                notify_visit(ip, request.path, device_type)

        except OperationalError:
            db.session.rollback()
        except Exception as e:
            app.logger.error(f"Tracking error: {e}")
            db.session.rollback()

    # Context Processor for injecting site and SEO settings into all templates
    @app.context_processor
    def inject_settings():
        try:
            site_settings = SiteSettings.query.first()
            # If table exists but empty, provide mock.
            # If table doesn't exist (e.g. init db issues in some envs), catch OpError.
            if site_settings is None:
                site_settings = MockSiteSettings()

            # Fetch Global SEO Settings (index page acts as global)
            global_seo = SeoSettings.query.filter_by(page_name='index').first()
            if not global_seo:
                 seo_settings = MockSeoSettings()
            else:
                 seo_settings = global_seo

            # Fetch Page Specific SEO Settings
            page_seo = None
            if request.endpoint:
                # Extract page name from endpoint (e.g. 'main.about' -> 'about')
                current_page = request.endpoint.split('.')[-1]
                page_seo = SeoSettings.query.filter_by(page_name=current_page).first()

        except (OperationalError, Exception) as e:
            app.logger.error(f"Database Error in inject_settings: {e}")
            site_settings = MockSiteSettings()
            seo_settings = MockSeoSettings()
            page_seo = None

        return dict(
            site_settings=site_settings,
            seo_settings=seo_settings,
            page_seo=page_seo,
            whatsapp_number=app.config.get('WHATSAPP_NUMBER', ''),
            consultation_url=app.config.get('CONSULTATION_URL', '')
        )

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(451)
    def unavailable_for_legal_reasons(e):
        return render_template('errors/451.html'), 451

    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

    @app.errorhandler(403)
    def forbidden(e):
        return render_template('errors/403.html'), 403

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
