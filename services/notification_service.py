import requests
from flask import current_app
from models.settings import SiteSettings
from models import db
from datetime import date
import json

def send_telegram_notification(message, ip_to_ban=None):
    """
    Sends a notification message to the configured Telegram chat.
    Retrieves the bot token and chat ID from the SiteSettings table.

    Args:
        message (str): The message to send.
        ip_to_ban (str, optional): IP address to propose for banning.
    """
    try:
        # Retrieve settings from the database
        settings = SiteSettings.query.first()

        if not settings:
            current_app.logger.warning("Telegram Notification: SiteSettings not found.")
            return False

        token = settings.telegram_bot_token
        chat_id = settings.telegram_chat_id

        if not token or not chat_id:
            current_app.logger.warning("Telegram Notification: Token or Chat ID is missing in settings.")
            return False

        # Daily Greeting Logic
        today = date.today()
        if settings.last_telegram_greeting_date != today:
            message = f"👋 Bonjour Boss ! Voici les premières nouvelles de la journée :\n\n{message}"
            settings.last_telegram_greeting_date = today
            try:
                db.session.commit()
            except Exception as e:
                current_app.logger.error(f"Failed to update greeting date: {e}")
                db.session.rollback()

        url = f"https://api.telegram.org/bot{token}/sendMessage"

        payload = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "HTML"
        }

        # Add Ban Button if IP is provided
        if ip_to_ban:
            keyboard = {
                "inline_keyboard": [
                    [
                        {"text": "🚫 Bannir cette IP", "callback_data": f"ban_ip:{ip_to_ban}"}
                    ]
                ]
            }
            payload["reply_markup"] = json.dumps(keyboard)

        # Send the request
        response = requests.post(url, json=payload, timeout=10)

        if response.status_code == 200:
            return True
        else:
            current_app.logger.error(f"Telegram Notification Failed: {response.status_code} - {response.text}")
            return False

    except Exception as e:
        print(f"Erreur Telegram: {e}")
        current_app.logger.error(f"Telegram Error: {e}")
        return False

def notify_visit(ip, path):
    """
    Sends a notification about a new visit if enabled in settings.
    """
    try:
        settings = SiteSettings.query.first()
        if not settings or not settings.notify_on_visit:
            return

        message = (
            f"👀 <b>Nouveau visiteur</b> sur <code>{path}</code>\n"
            f"📍 IP: <code>{ip}</code>"
        )
        # We call send_telegram_notification directly but we might want to avoid
        # the greeting logic for *every* visit if it's too chatty,
        # but the requirement says "Daily Greeting" check is inside send_telegram_notification.
        # So the first visit of the day will trigger the greeting.
        send_telegram_notification(message)

    except Exception as e:
        current_app.logger.error(f"Error in notify_visit: {e}")
