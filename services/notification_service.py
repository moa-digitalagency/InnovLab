import requests
from flask import current_app
from models.settings import SiteSettings
from models import db
from datetime import date

def send_telegram_notification(message, disable_notification=False, reply_markup=None):
    try:
        settings = SiteSettings.query.first()
        if not settings or not settings.telegram_bot_token or not settings.telegram_chat_id:
            return False

        # --- LOGIQUE DAILY GREETING ---
        today = date.today()
        greeting = ""
        if settings.last_telegram_greeting_date != today:
            greeting = "👋 *Bonjour Boss !* Voici les premières nouvelles de la journée pour InnovLab :\n\n"
            settings.last_telegram_greeting_date = today
            db.session.commit()

        final_message = greeting + message

        url = f"https://api.telegram.org/bot{settings.telegram_bot_token}/sendMessage"
        payload = {
            "chat_id": settings.telegram_chat_id,
            "text": final_message,
            "parse_mode": "Markdown",
            "disable_notification": disable_notification
        }

        if reply_markup:
            payload["reply_markup"] = reply_markup

        requests.post(url, json=payload, timeout=10)
        return True
    except Exception as e:
        current_app.logger.error(f"Telegram Error: {e}")
        return False

def notify_visit(ip, path, device_type):
    try:
        settings = SiteSettings.query.first()
        if settings and settings.notify_on_visit:
            device_icon = "📱" if device_type != "desktop" else "💻"
            msg = f"👀 *Nouveau visiteur* {device_icon}\n📍 *IP:* `{ip}`\n🔗 *Page:* {path}"
            # On met disable_notification=True pour ne pas faire sonner le tel à chaque visite
            send_telegram_notification(msg, disable_notification=True)
    except Exception:
        pass
