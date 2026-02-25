from flask import Flask
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

    @app.context_processor
    def inject_settings():
        site_settings = SiteSettings.query.first()
        seo_settings_list = SeoSettings.query.all()
        seo_settings = {s.page_name: s for s in seo_settings_list}
        return dict(site_settings=site_settings, seo_settings=seo_settings)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
