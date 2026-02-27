import os

class Config:
    uri = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    # PostgreSQL Compatibility Fix
    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

    # Debug configuration
    DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')

    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'statics', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    WHATSAPP_NUMBER = os.getenv('WHATSAPP_NUMBER', '243860493345')
    CONSULTATION_URL = os.getenv('CONSULTATION_URL', 'https://tidycal.com/moamyoneart/consultation-gratuite-15-min')

    # Security Configuration
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'ChangeMeNow!')

    # i18n Configuration
    LANGUAGES = ['fr', 'en', 'es', 'pt', 'it', 'de', 'ar', 'zh', 'ja', 'ko']
