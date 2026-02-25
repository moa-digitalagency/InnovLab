from flask import Flask
from config.config import Config
from models import db
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='statics')
    app.config.from_object(Config)

    db.init_app(app)

    # Import and register blueprints/routes
    from routes.main import main_bp
    app.register_blueprint(main_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
