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
from werkzeug.middleware.proxy_fix import ProxyFix

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

    # Trust X-Forwarded-* headers from Nginx reverse proxy
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

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
    from services.i18n_service import get_locale, setup_i18n

    # Set up i18n
    setup_i18n(app)

    @app.before_request
    def handle_language():
        # Call get_locale to ensure session gets updated on every request
        # if there's a lang parameter
        get_locale()

    # 1. Banned IP Middleware (with caching to prevent DB queries on every request)
    banned_ips_cache = {'ips': set(), 'last_update': 0}
    BANNED_IP_CACHE_TTL = 300  # 5 minutes

    @app.before_request
    def block_banned_ips():
        import time
        try:
            ip = request.remote_addr
            current_time = time.time()

            # Refresh cache every 5 minutes instead of querying DB every request
            if current_time - banned_ips_cache['last_update'] > BANNED_IP_CACHE_TTL:
                try:
                    banned_ips_cache['ips'] = {row.ip_address for row in BannedIP.query.all()}
                    banned_ips_cache['last_update'] = current_time
                except OperationalError:
                    # Database might not be ready, use empty cache
                    banned_ips_cache['ips'] = set()

            # Check against cached IPs (no DB query)
            if ip and ip in banned_ips_cache['ips']:
                abort(403)
        except OperationalError:
            # Database might not be ready
            pass
        except Exception as e:
            app.logger.error(f"Error in block_banned_ips: {e}")

    # 2. Analytics Tracking Middleware - DISABLED (was causing 504 timeouts)
    # Visitor tracking is deferred to a background job to prevent blocking requests
    @app.before_request
    def track_visitor():
        """
        DISABLED: Visitor tracking has been moved to background processing.
        Previous implementation was querying database on every request,
        causing 504 timeouts. This placeholder prevents errors if code references this function.
        """
        pass

    # Context Processor for injecting site and SEO settings into all templates (with caching)
    settings_cache = {'site': None, 'seo': {}, 'last_update': 0}
    SETTINGS_CACHE_TTL = 3600  # 1 hour

    @app.context_processor
    def inject_settings():
        import time
        try:
            current_time = time.time()

            # Cache settings for 1 hour to avoid DB queries on every request
            if current_time - settings_cache['last_update'] > SETTINGS_CACHE_TTL:
                try:
                    site_settings = SiteSettings.query.first()
                    if site_settings is None:
                        site_settings = MockSiteSettings()
                    settings_cache['site'] = site_settings

                    # Fetch Global SEO Settings
                    global_seo = SeoSettings.query.filter_by(page_name='index').first()
                    if not global_seo:
                        seo_settings = MockSeoSettings()
                    else:
                        seo_settings = global_seo
                    settings_cache['seo']['global'] = seo_settings
                    settings_cache['last_update'] = current_time
                except OperationalError:
                    # Database not ready, use mock settings
                    if settings_cache['site'] is None:
                        settings_cache['site'] = MockSiteSettings()
                    if 'global' not in settings_cache['seo']:
                        settings_cache['seo']['global'] = MockSeoSettings()

            site_settings = settings_cache['site'] or MockSiteSettings()
            seo_settings = settings_cache['seo'].get('global') or MockSeoSettings()

            # Fetch Page Specific SEO Settings (cached in memory, not DB)
            page_seo = None
            if request.endpoint:
                # Extract page name from endpoint (e.g. 'main.about' -> 'about')
                current_page = request.endpoint.split('.')[-1]
                if current_page not in settings_cache['seo']:
                    try:
                        page_seo = SeoSettings.query.filter_by(page_name=current_page).first()
                        if page_seo:
                            settings_cache['seo'][current_page] = page_seo
                    except OperationalError:
                        page_seo = None
                else:
                    page_seo = settings_cache['seo'].get(current_page)

        except Exception as e:
            app.logger.error(f"Error in inject_settings: {e}")
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
