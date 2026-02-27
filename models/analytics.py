from . import db
from datetime import datetime

class VisitAnalytics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(45))  # IPv6 support
    user_agent = db.Column(db.String(256))
    path = db.Column(db.String(256))
    referrer = db.Column(db.String(256))
    device_type = db.Column(db.String(20), default='desktop')  # mobile/desktop
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<VisitAnalytics {self.path} - {self.ip_address}>'
