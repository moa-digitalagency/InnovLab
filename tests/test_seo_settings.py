import unittest
from app import app, db
from models.settings import SeoSettings, SiteSettings
from models.user import User

class SeoSettingsTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.drop_all()
            db.create_all()

            # Create admin user
            admin = User(username='admin')
            admin.set_password('admin')
            db.session.add(admin)

            # Create default settings
            settings = SiteSettings(site_title='Test Site')
            db.session.add(settings)

            # Create default SEO settings
            seo = SeoSettings(page_name='index', title_tag='Home')
            db.session.add(seo)

            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def login(self):
        return self.app.post('/admin/login', data=dict(
            username='admin',
            password='admin'
        ), follow_redirects=True)

    def test_seo_model_columns(self):
        with app.app_context():
            seo = SeoSettings.query.filter_by(page_name='index').first()
            self.assertTrue(hasattr(seo, 'og_site_name'))
            self.assertTrue(hasattr(seo, 'og_image_default'))
            self.assertTrue(hasattr(seo, 'twitter_handle'))

            # Test default values (SQLite defaults might not apply instantly without server restart or migration in memory,
            # but we can check if we can set them)
            seo.og_site_name = 'My Open Graph Site'
            seo.twitter_handle = '@MyTwitter'
            db.session.commit()

            updated_seo = SeoSettings.query.filter_by(page_name='index').first()
            self.assertEqual(updated_seo.og_site_name, 'My Open Graph Site')
            self.assertEqual(updated_seo.twitter_handle, '@MyTwitter')

    def test_admin_seo_route_get(self):
        self.login()
        response = self.app.get('/admin/seo')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Nom du site (Open Graph)', response.data)
        self.assertIn(b'Twitter Handle', response.data)
        self.assertIn(b'Image Open Graph par d', response.data)

    def test_admin_seo_route_post(self):
        self.login()
        response = self.app.post('/admin/seo', data={
            'og_site_name': 'Updated Site Name',
            'twitter_handle': '@UpdatedHandle'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Param', response.data) # Check for flash message part

        with app.app_context():
            seo = SeoSettings.query.filter_by(page_name='index').first()
            self.assertEqual(seo.og_site_name, 'Updated Site Name')
            self.assertEqual(seo.twitter_handle, '@UpdatedHandle')

if __name__ == '__main__':
    unittest.main()
