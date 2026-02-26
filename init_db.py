from app import app
from models import db, User, SiteSettings, SeoSettings, FounderRequest, StartupRequest, InvestorRequest, PortfolioProject, Contact, Message
import sys
import os
from sqlalchemy import inspect, text

def check_and_migrate():
    inspector = inspect(db.engine)

    # Determine boolean default based on dialect
    bool_default = "DEFAULT FALSE"
    if db.engine.name == 'sqlite':
        bool_default = "DEFAULT 0"

    # Define new columns to check
    schema_updates = {
        'site_settings': [
            ('header_logo', 'VARCHAR(256)'),
            ('footer_logo', 'VARCHAR(256)'),
            ('favicon', 'VARCHAR(256)'),
            ('custom_head_code', 'TEXT'),
            ('telegram_bot_token', 'VARCHAR(256)'),
            ('telegram_chat_id', 'VARCHAR(128)'),
            ('linkedin_url', 'VARCHAR(256)'),
            ('twitter_url', 'VARCHAR(256)'),
            ('facebook_url', 'VARCHAR(256)')
        ],
        'seo_settings': [
            ('meta_title_default', 'VARCHAR(256)'),
            ('meta_description_default', 'VARCHAR(512)'),
            ('meta_keywords_default', 'VARCHAR(256)'),
            ('google_analytics_id', 'VARCHAR(64)'),
            ('robots_txt_content', 'TEXT')
        ],
        'founder_request': [
            ('status', "VARCHAR(20) DEFAULT 'new'")
        ],
        'startup_request': [
            ('status', "VARCHAR(20) DEFAULT 'new'")
        ],
        'investor_request': [
            ('status', "VARCHAR(20) DEFAULT 'new'")
        ],
        'message': [
            ('read', f"BOOLEAN {bool_default}")
        ]
    }

    try:
        with db.engine.connect() as conn:
            for table_name, columns in schema_updates.items():
                if inspector.has_table(table_name):
                    existing_columns = [c['name'] for c in inspector.get_columns(table_name)]
                    for col_name, col_type in columns:
                        if col_name not in existing_columns:
                            print(f"Migrating: Adding {col_name} to {table_name}")
                            try:
                                conn.execute(text(f"ALTER TABLE {table_name} ADD COLUMN {col_name} {col_type}"))
                                conn.commit()
                            except Exception as e:
                                print(f"Error adding column {col_name} to {table_name}: {e}")
    except Exception as e:
        print(f"Migration check failed: {e}")

def init_database():
    with app.app_context():
        try:
            # Ensure all tables are created (idempotent)
            # db.drop_all() # Removed to prevent data loss - enabling migration mode
            db.create_all()
            print("Database tables verified.")

            check_and_migrate()

        except Exception as e:
            print(f"Error creating/migrating tables: {e}", file=sys.stderr)
            return

        try:
            inspector = inspect(db.engine)
            if inspector.has_table('user'):
                # Get admin credentials from config (loaded from environment variables)
                admin_username = app.config.get('ADMIN_USERNAME', 'admin')
                admin_password = app.config.get('ADMIN_PASSWORD', 'ChangeMeNow!')

                admin = User.query.filter_by(username=admin_username).first()
                if not admin:
                    print(f"Creating default admin user '{admin_username}'...")
                    new_admin = User(username=admin_username)
                    new_admin.set_password(admin_password)
                    db.session.add(new_admin)
                    db.session.commit()
                    print(f"Admin user created ({admin_username}).")
                else:
                    print(f"Admin user '{admin_username}' exists. Updating password from environment...")
                    admin.set_password(admin_password)
                    db.session.commit()
                    print(f"Admin password updated for '{admin_username}'.")
        except Exception as e:
            print(f"Error creating admin user: {e}", file=sys.stderr)

if __name__ == "__main__":
    init_database()
