import unittest
from flask import current_app
from app import create_app
from models import db
from models.settings import SiteSettings, SeoSettings

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()

        # Seed necessary data
        settings = SiteSettings(site_title='Test Site')
        db.session.add(settings)
        seo = SeoSettings(page_name='index')
        db.session.add(seo)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_public_routes(self):
        routes = ['/', '/about', '/services', '/portfolio', '/contact-us', '/candidature/founder']
        for route in routes:
            with self.subTest(route=route):
                response = self.client.get(route)
                self.assertEqual(response.status_code, 200, f"Route {route} failed")

    def test_admin_redirect(self):
        response = self.client.get('/admin/dashboard')
        self.assertEqual(response.status_code, 302)
        # Verify redirect location contains login
        self.assertTrue('/admin/login' in response.location)

    def test_login_page(self):
        response = self.client.get('/admin/login')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
