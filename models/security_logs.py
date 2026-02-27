from . import db
from datetime import datetime

class SecurityLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(45))
    event_type = db.Column(db.String(50))  # xss_attempt, spam_form, bot_scraping
    description = db.Column(db.Text)
    user_agent = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<SecurityLog {self.event_type} - {self.ip_address}>'

class BannedIP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(45), unique=True, nullable=False)
    reason = db.Column(db.Text)
    banned_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<BannedIP {self.ip_address}>'
