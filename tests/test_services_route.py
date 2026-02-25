
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
        self.assertIn(b'5. MISSIONS OP\xc3\x89RATIONNELLES & SERVICES', response.data)
        self.assertIn(b'Accompagnement & Incubation', response.data)
        self.assertIn(b'Shabaka Academy', response.data)

if __name__ == '__main__':
    unittest.main()
