import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'statics', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    WHATSAPP_NUMBER = os.getenv('WHATSAPP_NUMBER', '243860493345')
    CONSULTATION_URL = os.getenv('CONSULTATION_URL', 'https://tidycal.com/moamyoneart/consultation-gratuite-15-min')
