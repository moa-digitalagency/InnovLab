import unittest
from unittest.mock import patch, MagicMock
from app import create_app
from models import db
from sqlalchemy.exc import OperationalError

class TestResilience(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_homepage_resilience_empty_db(self):
        """
        Test that the homepage renders correctly even if the SiteSettings table is empty or DB fails,
        thanks to the robust inject_settings context processor.
        """
        # Ensure SiteSettings is empty (it should be in a fresh memory DB, but just in case)
        # We are simulating the "OperationalError" or simply empty return.

        # Mocking the query to raise an OperationalError to simulate DB failure
        with patch('models.settings.SiteSettings.query') as mock_query:
            mock_query.first.side_effect = OperationalError("Mock DB Error", "params", "orig")

            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            # Check if the default title from the Mock object is present
            self.assertIn(b'Shabaka InnovLab', response.data)

    def test_homepage_resilience_none_return(self):
        """
        Test that the homepage renders correctly if SiteSettings.query.first() returns None.
        """
        with patch('models.settings.SiteSettings.query') as mock_query:
            mock_query.first.return_value = None

            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Shabaka InnovLab', response.data)

    def test_contact_form_error_handling_none_return(self):
        """
        Test that the contact form submission handles service failures (None return) gracefully.
        """
        # Mock the service to return None (simulating failure)
        with patch('services.submission_service.SubmissionService.process_quick_contact') as mock_service:
            mock_service.return_value = None

            response = self.client.post('/contact', data={'email': 'test@example.com'}, follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            # Check for the error flash message
            self.assertIn("Une erreur interne est survenue".encode('utf-8'), response.data)

    def test_contact_form_exception_handling_with_rollback(self):
        """
        Test that the contact form submission handles unexpected exceptions gracefully
        and calls db.session.rollback().
        """
        # Mock the service to raise an Exception
        with patch('services.submission_service.SubmissionService.process_quick_contact') as mock_service:
            mock_service.side_effect = Exception("Unexpected service error")

            # Mock db.session.rollback to verify it's called
            with patch('routes.public.forms.db.session.rollback') as mock_rollback:
                response = self.client.post('/contact', data={'email': 'test@example.com'}, follow_redirects=True)

                self.assertEqual(response.status_code, 200)
                # Check for the error flash message
                self.assertIn("Une erreur interne est survenue".encode('utf-8'), response.data)
                # Verify rollback was called
                mock_rollback.assert_called_once()

if __name__ == '__main__':
    unittest.main()
