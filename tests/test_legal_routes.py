import unittest
from app import create_app, db
from models.settings import SiteSettings

class LegalRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            # Seed SiteSettings
            settings = SiteSettings(
                site_title="Test Site",
                privacy_policy="<p>Privacy Policy Content</p>",
                terms_conditions="<p>Terms Content</p>"
            )
            db.session.add(settings)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_privacy_policy_route(self):
        response = self.client.get('/privacy-policy')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Politique de Confidentialit', response.data)
        self.assertIn(b'Privacy Policy Content', response.data)

    def test_terms_conditions_route(self):
        response = self.client.get('/terms-conditions')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Conditions G', response.data)
        self.assertIn(b'Terms Content', response.data)

if __name__ == '__main__':
    unittest.main()
