from flask import Flask, render_template
from flask_login import LoginManager
from config.config import Config
from models import db, User
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='statics')
    app.config.from_object(Config)

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'admin.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Import and register blueprints/routes
    from routes.main import main_bp
    app.register_blueprint(main_bp)

    from routes.admin_routes import admin_bp
    app.register_blueprint(admin_bp)

    from models.settings import SiteSettings, SeoSettings

    # Context Processor for injecting site and SEO settings into all templates
    @app.context_processor
    def inject_settings():
        site_settings = SiteSettings.query.first()
        seo_settings_list = SeoSettings.query.all()
        seo_settings = {s.page_name: s for s in seo_settings_list}
        return dict(
            site_settings=site_settings,
            seo_settings=seo_settings,
            whatsapp_number=app.config['WHATSAPP_NUMBER'],
            consultation_url=app.config['CONSULTATION_URL']
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

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
