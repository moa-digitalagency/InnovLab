import unittest
import sys
import os

# Add the root directory to sys.path so we can import app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from models import db
from models.forms import FounderRequest, StartupRequest, InvestorRequest

class TestRoutes(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['WTF_CSRF_ENABLED'] = False # Disable CSRF for testing
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Futur Technologique', response.data)

    def test_founder_route(self):
        response = self.app.get('/candidature/founder')
        self.assertEqual(response.status_code, 200)
        # Check for title or specific text
        self.assertIn(b'Programme Fondateurs', response.data)

    def test_startup_route(self):
        response = self.app.get('/candidature/startup')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Programme Startups', response.data)

    def test_investor_route(self):
        response = self.app.get('/candidature/investor')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Investissez dans le Futur', response.data)

    def test_founder_submission(self):
        with app.app_context():
            data = {
                'nom': 'John Doe',
                'email': 'john@example.com',
                'projet_name': 'My Project',
                'description': 'Description'
            }
            response = self.app.post('/candidature/founder', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 200)

            # Verify database
            founder = FounderRequest.query.filter_by(email='john@example.com').first()
            self.assertIsNotNone(founder)
            self.assertEqual(founder.nom, 'John Doe')

    def test_startup_submission(self):
        with app.app_context():
            data = {
                'nom_startup': 'My Startup',
                'email': 'startup@example.com',
                'secteur': 'Tech',
                'besoins': 'Money'
            }
            response = self.app.post('/candidature/startup', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 200)

            # Verify database
            startup = StartupRequest.query.filter_by(email='startup@example.com').first()
            self.assertIsNotNone(startup)
            self.assertEqual(startup.nom_startup, 'My Startup')

    def test_investor_submission(self):
        with app.app_context():
            data = {
                'nom': 'Investor 1',
                'email': 'investor@example.com',
                'type_investisseur': 'VC',
                'ticket_moyen': '>1M'
            }
            response = self.app.post('/candidature/investor', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 200)

            # Verify database
            investor = InvestorRequest.query.filter_by(email='investor@example.com').first()
            self.assertIsNotNone(investor)
            self.assertEqual(investor.nom, 'Investor 1')

if __name__ == '__main__':
    unittest.main()
