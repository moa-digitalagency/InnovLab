import pytest
from app import create_app
from models import db
from models.testimonial import Testimonial

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    # Ensure TALISMAN doesn't force HTTPS
    app.config['TALISMAN_FORCE_HTTPS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def test_index_testimonials_display(client):
    """Test that testimonials are correctly displayed on the index page."""
    # Ensure correct app context and request context for url_for if needed, though client.get handles it.

    # 1. Setup Data: Create 1 featured and 2 standard testimonials
    featured = Testimonial(
        author_name='Featured Author',
        author_title='Featured Title',
        content='This is the featured testimonial.',
        is_featured=True
    )

    standard1 = Testimonial(
        author_name='Standard Author 1',
        author_title='Standard Title 1',
        content='This is standard testimonial 1.',
        is_featured=False
    )

    standard2 = Testimonial(
        author_name='Standard Author 2',
        author_title='Standard Title 2',
        content='This is standard testimonial 2.',
        is_featured=False
    )

    db.session.add_all([featured, standard1, standard2])
    db.session.commit()

    # 2. Request Index Page
    response = client.get('/')
    assert response.status_code == 200

    data = response.data.decode('utf-8')

    # 3. Verify Featured Testimonial (Blue Card) content
    assert 'Featured Author' in data
    assert 'Featured Title' in data
    assert 'This is the featured testimonial.' in data
    # Check for specific class indicating featured styling
    assert 'bg-[#064060]' in data

    # 4. Verify Standard Testimonials (White Cards) content
    assert 'Standard Author 1' in data
    assert 'Standard Title 1' in data
    assert 'This is standard testimonial 1.' in data

    assert 'Standard Author 2' in data
    assert 'Standard Title 2' in data
    assert 'This is standard testimonial 2.' in data

    # Check for specific class indicating standard styling (checking one instance is enough)
    # Note: bg-[#ffffff] is used for standard cards
    assert 'bg-[#ffffff]' in data

def test_index_testimonials_empty(client):
    """Test index page behavior with no testimonials."""
    response = client.get('/')
    assert response.status_code == 200

    data = response.data.decode('utf-8')

    # Ensure no Jinja2 errors and sections are just empty/hidden
    # Our template logic uses {% if ... %} blocks, so they should not render content if empty.
    assert 'Featured Author' not in data
