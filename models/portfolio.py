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

    def get_translation(self, field_name, lang_code='fr'):
        import json
        import logging
        try:
            val = getattr(self, field_name)
            if not val:
                return ""

            # Si c'est déjà un dictionnaire
            if isinstance(val, dict):
                return val.get(lang_code, val.get('fr', str(val)))

            # Si c'est du texte, on tente de voir si c'est du JSON stringifié
            if isinstance(val, str):
                val = val.strip()
                if val.startswith('{') and val.endswith('}'):
                    try:
                        data = json.loads(val)
                        return data.get(lang_code, data.get('fr', str(data)))
                    except json.JSONDecodeError:
                        return val # Fallback si JSON invalide
                return val # Fallback si vieux texte classique

            return str(val)
        except Exception as e:
            logging.error(f"Erreur get_translation sur {field_name}: {e}")
            return ""

    def __repr__(self):
        return f'<PortfolioProject {self.id}>'
