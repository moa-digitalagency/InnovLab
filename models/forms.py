from . import db
from datetime import datetime

class FounderRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(128))
    email = db.Column(db.String(120))
    projet_name = db.Column(db.String(128))
    description = db.Column(db.Text)
    file_pitch = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<FounderRequest {self.projet_name}>'

class StartupRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom_startup = db.Column(db.String(128))
    email = db.Column(db.String(120))
    secteur = db.Column(db.String(128))
    besoins = db.Column(db.Text)
    website_url = db.Column(db.String(256))
    stage = db.Column(db.String(64))
    file_pitch = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<StartupRequest {self.nom_startup}>'

class InvestorRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(128))
    email = db.Column(db.String(120))
    type_investisseur = db.Column(db.String(64))
    ticket_moyen = db.Column(db.String(64))
    sectors_interest = db.Column(db.String(256))
    linkedin_profile = db.Column(db.String(256))
    file_intent = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<InvestorRequest {self.nom}>'
