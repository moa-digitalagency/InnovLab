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
        import json
        val = getattr(self, field_name)
        if not val:
            return ""
        try:
            # Si c'est déjà un dictionnaire
            if isinstance(val, dict):
                return val.get(lang_code, val.get('fr', ''))
            # Si c'est une chaîne de caractères ressemblant à du JSON
            elif isinstance(val, str) and val.startswith('{'):
                data = json.loads(val)
                return data.get(lang_code, data.get('fr', ''))
            # Si c'est du vieux texte standard (Fallback)
            else:
                return str(val)
        except Exception:
            return str(val)

    def __repr__(self):
        return f'<PortfolioProject {self.id}>'
