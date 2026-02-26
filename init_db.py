from app import app
from models import db, User
import sys
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
            db.create_all()
            print("Database tables created.")

            check_and_migrate()

        except Exception as e:
            print(f"Error creating tables: {e}", file=sys.stderr)
            return

        try:
            inspector = inspect(db.engine)
            if inspector.has_table('user'):
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
