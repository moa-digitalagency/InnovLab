import sys
import os
import argparse
from sqlalchemy.exc import IntegrityError

# Add the parent directory to sys.path to allow importing from the app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app
from models import db, User

def create_admin(username, password):
    """
    Creates an admin user with the given username and password.
    """
    with app.app_context():
        try:
            existing_user = User.query.filter_by(username=username).first()
            if existing_user:
                print(f"Error: User '{username}' already exists.")
                return False

            new_admin = User(username=username)
            new_admin.set_password(password)
            db.session.add(new_admin)
            db.session.commit()
            print(f"Success: Admin user '{username}' created successfully.")
            return True

        except IntegrityError:
            db.session.rollback()
            print(f"Error: Database integrity error. User '{username}' might already exist.")
            return False
        except Exception as e:
            db.session.rollback()
            print(f"Error: An unexpected error occurred: {e}")
            return False

def main():
    parser = argparse.ArgumentParser(description="Create a new admin user manually.")
    parser.add_argument("username", help="The username for the new admin.")
    parser.add_argument("password", help="The password for the new admin.")

    args = parser.parse_args()

    create_admin(args.username, args.password)

if __name__ == "__main__":
    main()
