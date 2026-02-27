from flask import url_for
from models import db
from models.security_logs import SecurityLog, BannedIP
from models.contact import Contact
import pytest

def test_csrf_protection(client, app):
    """Test that forms are protected by CSRF."""
    # Ensure CSRF is enabled
    app.config['WTF_CSRF_ENABLED'] = True
    response = client.post('/contact', data={'email': 'test@example.com'})
    # It might return 400 Bad Request directly
    assert response.status_code == 400 or b'CSRF' in response.data

def test_honeypot_logic(client, app):
    """Test that filling the honeypot field triggers the trap."""
    # Temporarily disable CSRF to test honeypot logic specifically,
    # or we would need to fetch a token first.
    app.config['WTF_CSRF_ENABLED'] = False

    data = {
        'email': 'spambot@example.com',
        'website_url_check': 'I am a bot'
    }

    # follow_redirects=True follows to the destination.
    response = client.post('/contact', data=data, follow_redirects=True)

    # Check status code of the response
    assert response.status_code == 200
    # Check for the flash message text in the response
    # The message is flashed, so it should be in the page content
    assert b'Merci pour votre inscription' in response.data

    with app.app_context():
        # Ensure it wasn't saved
        contact = Contact.query.filter_by(email='spambot@example.com').first()
        assert contact is None

        # Ensure it was logged
        log = SecurityLog.query.filter_by(event_type='spam_honeypot').first()
        assert log is not None
        assert 'Honeypot field filled' in log.description

    app.config['WTF_CSRF_ENABLED'] = True

def test_banned_ip_middleware(client, app):
    """Test that banned IPs are rejected."""
    ip = '123.123.123.123'
    with app.app_context():
        banned = BannedIP(ip_address=ip, reason='Test Ban')
        db.session.add(banned)
        db.session.commit()

    # Simulate request from banned IP
    response = client.get('/', environ_base={'REMOTE_ADDR': ip})
    # BannedIP middleware aborts with 403
    assert response.status_code == 403

def test_rate_limiting(client, app):
    """Test rate limiting on form routes."""
    app.config['WTF_CSRF_ENABLED'] = False
    # Use a fresh IP for rate limiting test to avoid overlap with other tests
    ip = '10.0.0.10'

    # Limit is 5 per minute.
    # 1
    client.post('/contact', data={'email': 'rate@test.com'}, environ_base={'REMOTE_ADDR': ip})
    # 2
    client.post('/contact', data={'email': 'rate@test.com'}, environ_base={'REMOTE_ADDR': ip})
    # 3
    client.post('/contact', data={'email': 'rate@test.com'}, environ_base={'REMOTE_ADDR': ip})
    # 4
    client.post('/contact', data={'email': 'rate@test.com'}, environ_base={'REMOTE_ADDR': ip})
    # 5
    client.post('/contact', data={'email': 'rate@test.com'}, environ_base={'REMOTE_ADDR': ip})

    # 6th request should fail
    response = client.post('/contact', data={'email': 'rate@test.com'}, environ_base={'REMOTE_ADDR': ip})

    # Flask-Limiter returns 429 Too Many Requests
    assert response.status_code == 429

    app.config['WTF_CSRF_ENABLED'] = True
