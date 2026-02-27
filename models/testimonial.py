from . import db
from datetime import datetime

class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(128), nullable=False)
    author_title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    is_featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Testimonial {self.author_name}>'
