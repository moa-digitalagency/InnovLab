import pytest
from app import create_app
from flask import session

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "WTF_CSRF_ENABLED": False,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })
    from models import db
    with app.app_context():
        db.create_all()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_default_locale(client):
    response = client.get('/')
    assert response.status_code == 200

def test_locale_selector_url(client):
    response = client.get('/?lang=en')
    assert response.status_code == 200
    with client.session_transaction() as sess:
        assert sess['lang'] == 'en'

def test_invalid_locale_selector_url(client):
    response = client.get('/?lang=xx')
    assert response.status_code == 200
    with client.session_transaction() as sess:
        assert 'lang' not in sess or sess['lang'] != 'xx'
