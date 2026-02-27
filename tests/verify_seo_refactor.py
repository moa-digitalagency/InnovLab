import unittest
from flask import Flask, template_rendered
from app import create_app, db
from models.settings import SiteSettings, SeoSettings

class TestSeoRefactor(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()

        # Seed Site Settings (Required for context processor)
        site_settings = SiteSettings(
            site_title="Shabaka Test",
            contact_email="test@shabaka.com",
            favicon="img/favicon.ico"
        )
        db.session.add(site_settings)

        # Seed Global SEO (Index)
        global_seo = SeoSettings(
            page_name='index',
            title_tag='Global Title',
            meta_desc='Global Description',
            meta_title_default='Default Global Title',
            meta_description_default='Default Global Description',
            meta_keywords_default='global, keywords',
            og_site_name='Global Site Name',
            og_image_default='img/global-og.jpg',
            twitter_handle='@GlobalHandle',
            google_analytics_id='G-TEST1234'
        )
        db.session.add(global_seo)

        # Seed Page Specific SEO (About)
        about_seo = SeoSettings(
            page_name='about',
            title_tag='About Us Title',
            meta_desc='About Us Description'
        )
        db.session.add(about_seo)

        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def test_global_defaults_on_index(self):
        """Test that the index page uses the global defaults (or index specific if set)."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        html = response.data.decode('utf-8')

        # In our implementation:
        # page_seo is the object for 'index' page.
        # title logic: {{ page_seo.title_tag if ... else seo_settings.meta_title_default }}
        # Since we set title_tag='Global Title' for index, it should appear.
        self.assertIn('<title>Global Title</title>', html)
        self.assertIn('content="Global Description"', html)

        # Verify OG Tags
        self.assertIn('property="og:site_name" content="Global Site Name"', html)
        # Verify default OG Image
        self.assertIn('img/global-og.jpg', html)
        # Verify Twitter
        self.assertIn('content="@GlobalHandle"', html)
        # Verify Analytics
        self.assertIn("G-TEST1234", html)

    def test_page_specific_override(self):
        """Test that the about page overrides the defaults."""
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        html = response.data.decode('utf-8')

        # About page has specific title_tag and meta_desc
        self.assertIn('<title>About Us Title</title>', html)
        self.assertIn('content="About Us Description"', html)

        # It relies on global defaults for other fields like OG Site Name
        self.assertIn('property="og:site_name" content="Global Site Name"', html)

        # Verify Self-Referencing OG Title (should match the page title)
        self.assertIn('property="og:title" content="About Us Title"', html)

    def test_fallback_behavior(self):
        """Test a page with NO specific settings uses global defaults."""
        # Create a route for a page with no SEO entry
        # services page exists in routes/public/navigation.py but we didn't seed it in DB
        response = self.client.get('/services')
        self.assertEqual(response.status_code, 200)
        html = response.data.decode('utf-8')

        # Should fallback to meta_title_default
        self.assertIn('<title>Default Global Title</title>', html)
        self.assertIn('content="Default Global Description"', html)

if __name__ == '__main__':
    unittest.main()
