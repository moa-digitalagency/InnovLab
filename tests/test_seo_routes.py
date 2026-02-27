import unittest
from flask import url_for
from app import create_app
from models import db
from models.settings import SeoSettings, SiteSettings

class TestSeoRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()

        # Seed minimal data
        db.session.add(SiteSettings(site_title='Test Site'))
        db.session.add(SeoSettings(page_name='index'))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_robots_txt_default(self):
        response = self.client.get('/robots.txt')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'text/plain')
        content = response.data.decode('utf-8')
        self.assertIn('User-agent: *', content)
        self.assertIn('Disallow: /admin/', content)
        self.assertIn('Sitemap:', content)
        self.assertIn('/sitemap.xml', content)

    def test_sitemap_xml(self):
        response = self.client.get('/sitemap.xml')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/xml')
        content = response.data.decode('utf-8')

        # Verify XML structure
        self.assertIn('<?xml version="1.0" encoding="UTF-8"?>', content)
        self.assertIn('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">', content)

        # Verify presence of key URLs
        expected_endpoints = [
            '/',
            '/about',
            '/services',
            '/portfolio',
            '/contact-us',
            '/candidature/startup',
            '/candidature/founder',
            '/candidature/investor'
        ]

        for endpoint in expected_endpoints:
            # Note: url_for with _external=True in test client might return http://localhost/endpoint
            # We check for the endpoint path at least
            self.assertIn(f'<loc>http://localhost{endpoint}</loc>', content)

        # Verify priority (sample)
        self.assertIn('<priority>1.0</priority>', content)
        self.assertIn('<priority>0.9</priority>', content)

if __name__ == '__main__':
    unittest.main()
