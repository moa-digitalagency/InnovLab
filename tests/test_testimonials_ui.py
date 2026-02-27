import pytest
from app import create_app
from models import db, User
from models.testimonial import Testimonial

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # Create admin user
            admin = User(id=1, username='admin')
            admin.set_password('password')
            db.session.add(admin)
            db.session.commit()
            yield client
            db.session.remove()
            db.drop_all()

def login(client, username, password):
    # Ensure force login logic if standard login fails in test env
    # Using 'admin' blueprint url for login
    return client.post('/admin/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)

def test_admin_testimonials_ui(client):
    """Test the testimonials UI elements and basic functionality."""
    login(client, 'admin', 'password')

    # 1. Access index
    response = client.get('/admin/testimonials/')
    assert response.status_code == 200
    assert b'T\xc3\xa9moignages' in response.data # "Témoignages"

    # Verify Sidebar link icon (using the layout modification)
    # We look for the link that points to the index and check if it contains the star icon
    assert b'<span class="material-symbols-outlined">star</span>' in response.data

    # 2. Add a testimonial
    response = client.post('/admin/testimonials/add', data={
        'author_name': 'Test User',
        'author_title': 'CEO',
        'content': 'Great service!'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Test User' in response.data
    assert b'Great service!' in response.data

    # 3. Verify Feature Button (Initial state: Unfeatured -> star_outline)
    # We look for the button with star_outline which indicates it is NOT featured
    assert b'star_outline' in response.data

    # Get the testimonial ID
    testimonial = Testimonial.query.first()
    assert testimonial is not None

    # 4. Feature the testimonial
    response = client.post(f'/admin/testimonials/feature/{testimonial.id}', follow_redirects=True)
    assert response.status_code == 200

    # Verify it's now featured in the UI (should have 'star' icon and be yellow)
    # The rendered HTML should have class "text-yellow-400" and icon "star"
    assert b'text-yellow-400' in response.data
    # We need to be careful not to match the sidebar icon again, but the sidebar icon is white/blue-ish.
    # The featured button is specifically yellow.
    assert b'<span class="material-symbols-outlined">star</span>' in response.data

    # 5. Verify Delete Button Exists
    assert b'/delete/' in response.data
    assert b'delete' in response.data # material icon name
