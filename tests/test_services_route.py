
import unittest
from app import create_app, db
from flask import url_for

class TestServicesRoute(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_services_page_loads(self):
        response = self.client.get('/services')
        self.assertEqual(response.status_code, 200)
        # Check for the new title (Missions Opérationnelles & Services)
        # Note: UTF-8 encoding for accents
        self.assertIn('Missions Opérationnelles & Services'.encode('utf-8'), response.data)
        self.assertIn(b'Accompagnement & Incubation', response.data)
        self.assertIn(b'Shabaka Academy', response.data)

    def test_contact_redirect(self):
        """Test that GET /contact redirects to homepage anchor."""
        response = self.client.get('/contact')
        # Check for 302 Found (redirect)
        self.assertEqual(response.status_code, 302)
        # Check the location header, it should point to /#contact or similar
        # Since we use url_for('main.index', _anchor='contact'), it should be /#contact
        # Need to handle potential full URL vs path
        location = response.headers['Location']
        self.assertTrue(location.endswith('/#contact') or location.endswith('index.html#contact'))

if __name__ == '__main__':
    unittest.main()
