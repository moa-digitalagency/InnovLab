from . import db

class SiteSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site_title = db.Column(db.String(128))
    meta_description = db.Column(db.String(256))
    contact_email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(256))

    # Images
    header_logo = db.Column(db.String(256))
    footer_logo = db.Column(db.String(256))
    favicon = db.Column(db.String(256))

    # Telegram
    telegram_bot_token = db.Column(db.String(256))
    telegram_chat_id = db.Column(db.String(128))

    # Social Media
    linkedin_url = db.Column(db.String(256))
    twitter_url = db.Column(db.String(256))
    facebook_url = db.Column(db.String(256))

    def __repr__(self):
        return f'<SiteSettings {self.site_title}>'

class SeoSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page_name = db.Column(db.String(64), unique=True)
    title_tag = db.Column(db.String(128))
    meta_desc = db.Column(db.String(256))
    keywords = db.Column(db.String(256))

    # Defaults & Analytics
    meta_title_default = db.Column(db.String(256))
    meta_description_default = db.Column(db.String(512))
    meta_keywords_default = db.Column(db.String(256))
    google_analytics_id = db.Column(db.String(64))
    robots_txt_content = db.Column(db.Text)

    def __repr__(self):
        return f'<SeoSettings {self.page_name}>'
