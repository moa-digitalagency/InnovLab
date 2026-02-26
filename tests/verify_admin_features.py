import unittest
import os
import io
from app import create_app
from models import db, User
from models.settings import SiteSettings, SeoSettings

class AdminFeaturesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing

        # Use a temporary upload folder
        self.test_upload_folder = os.path.join(self.app.root_path, 'statics', 'uploads', 'logos')
        if not os.path.exists(self.test_upload_folder):
            os.makedirs(self.test_upload_folder)

        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        # Create Admin User
        user = User(username='admin')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()

        # Create Initial Settings to avoid NoneType errors if logic expects them
        # (Though route creates them if missing, good to test that too)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        # Clean up files - optional but good practice.
        # For simplicity in this run, we might leave them or just delete the specific test file.

    def login(self):
        return self.client.post('/admin/login', data=dict(
            username='admin',
            password='password'
        ), follow_redirects=True)

    def test_settings_update_and_upload(self):
        self.login()

        # Mock file
        data = {
            'header_logo': (io.BytesIO(b"fake image content"), 'test_header_logo.png'),
            'contact_email': 'new_email@example.com',
            'telegram_bot_token': '123:ABC',
            'telegram_chat_id': '-100',
            'linkedin_url': 'https://linkedin.com/in/test'
        }

        response = self.client.post('/admin/settings', data=data, content_type='multipart/form-data', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Param&#232;tres du site mis &#224; jour', response.data.replace(b'\xc3\xa8', b'&#232;').replace(b'\xc3\xa0', b'&#224;'))
        # Note: Flash message encoding might vary, checking status and DB is safer.

        # Verify DB
        settings = SiteSettings.query.first()
        self.assertEqual(settings.contact_email, 'new_email@example.com')
        self.assertEqual(settings.telegram_bot_token, '123:ABC')
        self.assertEqual(settings.linkedin_url, 'https://linkedin.com/in/test')
        self.assertEqual(settings.header_logo, 'uploads/logos/test_header_logo.png')

        # Verify File
        file_path = os.path.join(self.test_upload_folder, 'test_header_logo.png')
        self.assertTrue(os.path.exists(file_path))

        # Clean up file
        os.remove(file_path)

    def test_seo_update(self):
        self.login()

        # Initial SEO setup (route creates index entry if missing, but we are posting)
        # We need to make sure the page entries exist or rely on the route logic.
        # The route logic creates them on GET, but here we POST immediately.
        # Let's hit GET first to trigger creation
        self.client.get('/admin/seo')

        data = {
            'google_analytics_id': 'G-TEST1234',
            'robots_txt_content': 'User-agent: Test\nDisallow: /test',
            'meta_title_default': 'Default Title',
            'title_index': 'Home Title'
        }

        response = self.client.post('/admin/seo', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Verify DB
        seo_index = SeoSettings.query.filter_by(page_name='index').first()
        self.assertIsNotNone(seo_index)
        self.assertEqual(seo_index.google_analytics_id, 'G-TEST1234')
        self.assertEqual(seo_index.robots_txt_content, 'User-agent: Test\nDisallow: /test')
        self.assertEqual(seo_index.title_tag, 'Home Title')

    def test_robots_txt_route(self):
        # Setup DB state
        seo = SeoSettings(page_name='index', robots_txt_content='User-agent: Bot\nDisallow: /secret')
        db.session.add(seo)
        db.session.commit()

        response = self.client.get('/robots.txt')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'text/plain')
        self.assertEqual(response.data, b'User-agent: Bot\nDisallow: /secret')

if __name__ == '__main__':
    unittest.main()
