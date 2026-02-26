from app import app
from models import db, User
import sys

def init_database():
    with app.app_context():
        try:
            db.create_all()
            print("Database tables created.")
        except Exception as e:
            print(f"Error creating tables: {e}", file=sys.stderr)
            return

        try:
            admin = User.query.filter_by(username='admin').first()
            if not admin:
                print("Creating default admin user...")
                new_admin = User(username='admin')
                new_admin.set_password('admin')
                db.session.add(new_admin)
                db.session.commit()
                print("Admin user created (admin/admin).")
            else:
                print("Admin user already exists.")
        except Exception as e:
            print(f"Error creating admin user: {e}", file=sys.stderr)

if __name__ == "__main__":
    init_database()
