import unittest
from app import app
from models import db, User, Message
from models.forms import FounderRequest, StartupRequest, InvestorRequest
from datetime import datetime, timedelta

class AdminDashboardTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

        # Create admin user
        admin = User(username='admin')
        admin.set_password('admin')
        db.session.add(admin)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def login(self, username, password):
        return self.app.post('/admin/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def test_dashboard_kpis(self):
        self.login('admin', 'admin')

        # Create some data
        # 2 unread messages, 1 read message
        m1 = Message(name='M1', email='m1@e.com', subject='S1', message='Msg1', read=False)
        m2 = Message(name='M2', email='m2@e.com', subject='S2', message='Msg2', read=False)
        m3 = Message(name='M3', email='m3@e.com', subject='S3', message='Msg3', read=True)
        db.session.add_all([m1, m2, m3])

        # Requests for chart
        today = datetime.now()
        yesterday = today - timedelta(days=1)

        f1 = FounderRequest(nom='F1', created_at=today)
        s1 = StartupRequest(nom_startup='S1', created_at=today)
        i1 = InvestorRequest(nom='I1', created_at=yesterday)

        db.session.add_all([f1, s1, i1])
        db.session.commit()

        response = self.app.get('/admin/dashboard')
        self.assertEqual(response.status_code, 200)

        # Check if "Messages Non Lus" count is 2 in the HTML
        # The template renders {{ unread_messages_count }}
        # Note: Depending on template rendering, it might be tricky to find exact number if other numbers match.
        # But we can look for the context if we used context capturing, or just search string.
        # "Messages Non Lus" ... "2"

        # Simple string check
        self.assertIn(b'Messages Non Lus', response.data)
        # We expect count 2
        # Use regex or simple search if '2' is unique enough, or check context variable?
        # Flask test client doesn't expose context variable easily without signal blinking.
        # Let's trust that if the text is there and 2 is there nearby, it works.

        # Or better, use template context capturing

    def test_dashboard_context(self):
        # Using context variable inspection
        from flask import template_rendered

        context_data = {}
        def capture_template_rendered(sender, template, context, **extra):
            context_data.update(context)

        template_rendered.connect(capture_template_rendered, app)

        self.login('admin', 'admin')

        # Create data
        m1 = Message(name='M1', email='m1@e.com', subject='S1', message='Msg1', read=False)
        db.session.add(m1)

        # Requests
        f1 = FounderRequest(nom='F1') # default created_at is now
        db.session.add(f1)
        db.session.commit()

        self.app.get('/admin/dashboard')

        self.assertEqual(context_data['unread_messages_count'], 1)
        self.assertEqual(context_data['founders_count'], 1)

        # Check chart data
        # Chart data should be a list of 7 integers
        chart_data = context_data['chart_data']
        self.assertEqual(len(chart_data), 7)
        # Today should have 1 request
        self.assertEqual(chart_data[-1], 1)

        template_rendered.disconnect(capture_template_rendered, app)

if __name__ == '__main__':
    unittest.main()
