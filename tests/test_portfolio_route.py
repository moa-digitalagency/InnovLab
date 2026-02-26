import unittest
from app import create_app, db

class TestPortfolioRoute(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_portfolio_page_loads(self):
        from models.portfolio import PortfolioProject

        # Seed database with a sample project
        with self.app.app_context():
            project = PortfolioProject(
                title="Shabaka Syndic",
                category="PropTech",
                description="Gestion de copropriété simplifiée.",
                project_url="https://shabakasyndic.ma",
                is_active=True
            )
            db.session.add(project)

            project2 = PortfolioProject(
                title="GovTech Project",
                category="GovTech",
                description="Description GovTech",
                project_url="#",
                is_active=True
            )
            db.session.add(project2)

            project3 = PortfolioProject(
                title="HealthTech Project",
                category="HealthTech",
                description="Description HealthTech",
                project_url="#",
                is_active=True
            )
            db.session.add(project3)

            project4 = PortfolioProject(
                title="Retail Project",
                category="Retail/Daily",
                description="Description Retail",
                project_url="#",
                is_active=True
            )
            db.session.add(project4)

            db.session.commit()

        response = self.client.get('/portfolio')
        self.assertEqual(response.status_code, 200)
        self.assertIn('NOS RÉALISATIONS'.encode('utf-8'), response.data)
        self.assertIn(b'Shabaka Syndic', response.data)
        self.assertIn(b'PropTech', response.data)
        self.assertIn(b'GovTech', response.data)
        self.assertIn(b'HealthTech', response.data)
        # Retail/Daily might be encoded differently if I didn't handle encoding carefully, but it's ASCII so should be fine.
        # Wait, 'Retail/Daily' contains '/', which is ASCII.
        self.assertIn(b'Retail/Daily', response.data)

if __name__ == '__main__':
    unittest.main()
