import os
import sys
import unittest
import re
from flask import url_for

# Add project root to sys.path to allow imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from models import db, User
from models.forms import StartupRequest
from models.settings import SiteSettings

class DeploymentVerification(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()
        self.ctx = app.app_context()
        self.ctx.push()

        # Ensure DB tables exist
        db.create_all()

        # Create Admin User
        admin_username = app.config.get('ADMIN_USERNAME', 'admin')
        admin_password = app.config.get('ADMIN_PASSWORD', 'admin')

        if not User.query.filter_by(username=admin_username).first():
            admin = User(username=admin_username)
            admin.set_password(admin_password)
            db.session.add(admin)
            db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def test_01_homepage_and_static_files(self):
        """Test homepage loads (200 OK) and all linked static files exist."""
        print("\n[TEST] Verifying Homepage and Static Assets...")
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200, "Homepage did not return 200 OK")

        html = response.data.decode('utf-8')

        # Regex to find static files in href="..." and src="..."
        # Looking for /static/... or /statics/...
        static_links = set(re.findall(r'(?:href|src)=["\'](/statics?/[^"\']+)["\']', html))

        if not static_links:
            print("WARNING: No static links found on homepage. HTML Content snippet:")
            print(html[:1000]) # Print first 1000 chars to debug

        missing_files = []
        for link in static_links:
            print(f"  Checking static asset: {link}")
            res = self.client.get(link)
            if res.status_code != 200:
                print(f"  [ERROR] Static file not found: {link} (Status: {res.status_code})")
                missing_files.append(link)
            else:
                print(f"  [OK] {link}")

        if missing_files:
            self.fail(f"Static files missing: {missing_files}")

    def test_02_startup_form_submission(self):
        """Test Startup Form submission and DB persistence."""
        print("\n[TEST] Verifying Startup Form Submission...")

        form_data = {
            'nom_startup': 'Test Startup Verif',
            'email': 'test_verif@startup.com',
            'secteur': 'Tech',
            'besoins': 'Funding',
            'website_url': 'http://example.com',
            'annual_revenue': '0-10k',
            'team_size': '1-5',
            'stage': 'Idea',
        }

        response = self.client.post('/candidature/startup', data=form_data, follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Form submission failed")

        startup = StartupRequest.query.filter_by(email='test_verif@startup.com').first()
        self.assertIsNotNone(startup, "Startup record not found in database")
        print(f"  [OK] Startup record created: {startup}")

    def test_03_admin_auth(self):
        """Test Admin Login and Dashboard Access."""
        print("\n[TEST] Verifying Admin Authentication...")

        username = app.config.get('ADMIN_USERNAME', 'admin')
        password = app.config.get('ADMIN_PASSWORD', 'admin')

        # 1. Login
        response = self.client.post('/admin/login', data={
            'username': username,
            'password': password
        }, follow_redirects=True)

        # Check if login successful (redirected to dashboard)
        # Dashboard page likely contains "Dashboard" or specific admin content
        if b'Invalid username' in response.data:
             self.fail("Login failed with valid credentials")

        self.assertEqual(response.status_code, 200)
        # Verify we are on dashboard
        self.assertIn(b'Dashboard', response.data, "Did not land on Dashboard after login")
        print("  [OK] Admin Dashboard accessible")

if __name__ == '__main__':
    unittest.main()
