import os
import sys

class Config:
    uri = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    # PostgreSQL Compatibility Fix
    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 300
    }
    
    # SECRET_KEY — MUST be set via environment variable
    SECRET_KEY = os.getenv('SECRET_KEY')
    if not SECRET_KEY:
        is_prod = os.getenv('FLASK_ENV', 'development') == 'production'
        if is_prod or os.getenv('ENFORCE_SECRET_KEY'):
            raise RuntimeError(
                "❌ CRITICAL: SECRET_KEY not configured.\n"
                "   Set the SECRET_KEY environment variable.\n"
                "   Example: export SECRET_KEY='your-very-long-random-key-here'"
            )
        # Development fallback (NOT for production)
        SECRET_KEY = 'dev-key-change-in-production-DO-NOT-USE-IN-PROD'

    # Debug configuration
    DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')

    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'statics', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    WHATSAPP_NUMBER = os.getenv('WHATSAPP_NUMBER', '243860493345')
    CONSULTATION_URL = os.getenv('CONSULTATION_URL', 'https://tidycal.com/moamyoneart/consultation-gratuite-15-min')

    # Security Configuration — MUST be set via environment variables
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
    
    if not ADMIN_USERNAME or not ADMIN_PASSWORD:
        is_prod = os.getenv('FLASK_ENV', 'development') == 'production'
        if is_prod or os.getenv('ENFORCE_ADMIN_CREDENTIALS'):
            raise RuntimeError(
                "❌ CRITICAL: Admin credentials not configured.\n"
                "   Set ADMIN_USERNAME and ADMIN_PASSWORD environment variables.\n"
                "   Example: export ADMIN_USERNAME='your-secure-username'\n"
                "   Example: export ADMIN_PASSWORD='your-very-strong-password'"
            )
        # Development fallback (NOT for production)
        ADMIN_USERNAME = ADMIN_USERNAME or 'admin'
        ADMIN_PASSWORD = ADMIN_PASSWORD or 'ChangeMeNow!'

    # Language Configuration
    LANGUAGES = ['fr', 'en', 'es', 'pt', 'it', 'de', 'ar', 'zh', 'ja', 'ko']
    
    # Logging Configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FORMAT = os.getenv('LOG_FORMAT', 'json')  # 'json' or 'text'
