import unittest
from app import create_app, db
from models.analytics import VisitAnalytics

class TestAnalyticsVerification(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        # Disable HTTPS redirect for testing
        self.app.debug = True

        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_visit_tracking(self):
        # Simulate a request to the homepage with a specific user agent
        user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'
        response = self.client.get('/', headers={'User-Agent': user_agent})

        # Verify the response is successful
        # 302 might happen if there's a redirect (e.g. trailing slash or https), but in testing it should be 200
        # If it is 302, let's see where it goes.
        if response.status_code == 302:
            print(f"Redirecting to: {response.headers['Location']}")
            response = self.client.get(response.headers['Location'], headers={'User-Agent': user_agent})

        self.assertEqual(response.status_code, 200)

        # Query the database for the visit record
        visit = VisitAnalytics.query.first()

        # Verify the record exists
        self.assertIsNotNone(visit, "Visit record should verify not be None")

        if visit:
            # Verify the details of the record
            # path might be / or /index depending on routing
            self.assertIn(visit.path, ['/', '/index'])
            self.assertEqual(visit.user_agent, user_agent)
            self.assertEqual(visit.device_type, 'mobile')
            # Referrer is 'Direct' when None
            self.assertEqual(visit.referrer, 'Direct')

    def test_admin_exclusion(self):
        # Simulate a request to an admin page
        # /admin/login is the standard login page
        response = self.client.get('/admin/login')

        # Check if a visit was recorded for admin path
        # Since we clear DB in setUp, if tracking worked for admin, we'd find it.
        # But we want to ensure it is NOT there.
        # Wait, the tracking happens BEFORE request processing.
        # So even if 404 or 302, it would track if not excluded.

        visit = VisitAnalytics.query.filter(VisitAnalytics.path.like('/admin%')).first()
        self.assertIsNone(visit, "Should not track admin pages")

if __name__ == '__main__':
    unittest.main()
