from . import db
from datetime import datetime

class PortfolioProject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.JSON, nullable=False)
    short_desc = db.Column(db.JSON, nullable=True)
    full_desc = db.Column(db.JSON, nullable=True)
    category = db.Column(db.JSON, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    project_url = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def get_translation(self, field_name, lang_code):
        value = getattr(self, field_name)
        if not value:
            return ""
        if isinstance(value, dict):
            return value.get(lang_code) or value.get('fr', "")
        return value

    def __repr__(self):
        return f'<PortfolioProject {self.id}>'
