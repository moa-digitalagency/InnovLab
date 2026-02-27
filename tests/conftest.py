import pytest
from app import create_app, db
from models.settings import SiteSettings, SeoSettings

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "DEBUG": True, # Ensure Talisman force_https is disabled
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": True,
        # Flask-Limiter config for testing
        "RATELIMIT_ENABLED": True,
        "RATELIMIT_STORAGE_URI": "memory://",
    })

    # Initialize app context
    with app.app_context():
        db.create_all()

        # Seed SiteSettings to avoid db error in context processor
        if not SiteSettings.query.first():
            settings = SiteSettings(site_title="Test Site")
            db.session.add(settings)

        if not SeoSettings.query.filter_by(page_name='index').first():
            seo = SeoSettings(page_name='index')
            db.session.add(seo)

        db.session.commit()

        yield app

        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
