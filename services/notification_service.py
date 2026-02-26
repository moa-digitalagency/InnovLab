import requests
from flask import current_app
from models.settings import SiteSettings

def send_telegram_notification(message):
    """
    Sends a notification message to the configured Telegram chat.
    Retrieves the bot token and chat ID from the SiteSettings table.
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

        url = f"https://api.telegram.org/bot{token}/sendMessage"

        payload = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }

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
