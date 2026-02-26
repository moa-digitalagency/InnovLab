import unittest
from flask import Flask
from models import db, SiteSettings
from utils.telegram_bot import send_telegram_notification
from unittest.mock import patch

class TestTelegramIntegration(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(self.app)

        with self.app.app_context():
            db.create_all()

    def test_notification_no_settings(self):
        with self.app.app_context():
            # Ensure table is empty
            db.session.query(SiteSettings).delete()
            db.session.commit()

            result = send_telegram_notification("Test Message")
            self.assertFalse(result)

    def test_notification_missing_credentials(self):
        with self.app.app_context():
            # Create settings but missing token/chat_id
            settings = SiteSettings(site_title="Test Site")
            db.session.add(settings)
            db.session.commit()

            result = send_telegram_notification("Test Message")
            self.assertFalse(result)

    @patch('utils.telegram_bot.requests.post')
    def test_notification_success(self, mock_post):
        with self.app.app_context():
            # Create settings with token/chat_id
            settings = SiteSettings(
                site_title="Test Site",
                telegram_bot_token="fake_token",
                telegram_chat_id="fake_chat_id"
            )
            db.session.add(settings)
            db.session.commit()

            # Mock success response
            mock_post.return_value.status_code = 200

            result = send_telegram_notification("Test Message")
            self.assertTrue(result)
            mock_post.assert_called_once()
            args, kwargs = mock_post.call_args
            self.assertIn("https://api.telegram.org/botfake_token/sendMessage", args[0])
            self.assertEqual(kwargs['json']['chat_id'], "fake_chat_id")
            self.assertEqual(kwargs['json']['text'], "Test Message")

if __name__ == '__main__':
    unittest.main()
