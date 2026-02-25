from . import db

class SiteSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site_title = db.Column(db.String(128))
    meta_description = db.Column(db.String(256))
    contact_email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(256))

    def __repr__(self):
        return f'<SiteSettings {self.site_title}>'

class SeoSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page_name = db.Column(db.String(64), unique=True)
    title_tag = db.Column(db.String(128))
    meta_desc = db.Column(db.String(256))
    keywords = db.Column(db.String(256))

    def __repr__(self):
        return f'<SeoSettings {self.page_name}>'
