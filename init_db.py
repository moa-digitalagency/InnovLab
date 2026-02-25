from app import app
from models import db, User

with app.app_context():
    db.create_all()
    print("Database tables created.")

    if not User.query.first():
        print("Creating default admin user...")
        admin = User(username='admin')
        admin.set_password('admin')
        db.session.add(admin)
        db.session.commit()
        print("Admin user created (admin/admin).")
    else:
        print("Admin user already exists.")
