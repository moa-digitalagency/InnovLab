from flask import Flask, render_template
from flask_login import LoginManager
from config.settings import Config
from models import db, User
from dotenv import load_dotenv
import os
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

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='statics')
    app.config.from_object(Config)

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
    app.register_blueprint(forms_bp)

    from routes.admin.auth import auth_bp
    app.register_blueprint(auth_bp)

    from routes.admin.dashboard import admin_bp
    app.register_blueprint(admin_bp)

    from routes.admin.portfolio import portfolio_bp
    app.register_blueprint(portfolio_bp)

    from routes.admin.settings import settings_bp
    app.register_blueprint(settings_bp)

    from models.settings import SiteSettings, SeoSettings

    # Context Processor for injecting site and SEO settings into all templates
    @app.context_processor
    def inject_settings():
        try:
            site_settings = SiteSettings.query.first()
            if site_settings is None:
                raise ValueError("SiteSettings table is empty")

            seo_settings_list = SeoSettings.query.all()
            seo_settings = {s.page_name: s for s in seo_settings_list}

        except (OperationalError, Exception) as e:
            app.logger.error(f"Database Error in inject_settings: {e}")
            site_settings = MockSiteSettings()
            seo_settings = {}

        return dict(
            site_settings=site_settings,
            seo_settings=seo_settings,
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
