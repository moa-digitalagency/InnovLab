from flask import Blueprint, request, jsonify, current_app
from models import db
from models.settings import SiteSettings
from models.security_logs import BannedIP
import requests
import hashlib

telegram_bp = Blueprint('telegram', __name__)

@telegram_bp.route('/webhook', methods=['POST'])
def webhook():
    """
    Webhook to handle Telegram updates.
    Verifies the X-Telegram-Bot-Api-Secret-Token header for security.
    """
    settings = SiteSettings.query.first()
    token = settings.telegram_bot_token if settings else None

    if not token:
         return jsonify({"status": "error", "message": "Configuration missing"}), 500

    # Verify Secret Token
    expected_secret = hashlib.sha256(token.encode()).hexdigest()
    incoming_secret = request.headers.get('X-Telegram-Bot-Api-Secret-Token')

    if incoming_secret != expected_secret:
        current_app.logger.warning(f"Unauthorized Webhook Attempt. IP: {request.remote_addr}")
        return jsonify({"status": "error", "message": "Unauthorized"}), 403

    update = request.get_json()
    if not update:
        return jsonify({"status": "error", "message": "No JSON payload"}), 400

    current_app.logger.info(f"Telegram Webhook received: {update}")

    if 'callback_query' in update:
        process_callback_query(update['callback_query'])

    return jsonify({"status": "success"}), 200

def process_callback_query(callback_query):
    """
    Processes the callback query from Telegram inline keyboard.
    """
    data = callback_query.get('data')
    message = callback_query.get('message')
    chat_id = message.get('chat', {}).get('id') if message else None
    callback_query_id = callback_query.get('id')

    if not data or not chat_id:
        return

    settings = SiteSettings.query.first()
    token = settings.telegram_bot_token if settings else None

    if not token:
        current_app.logger.error("Telegram Token not found in settings")
        return

    if data.startswith('ban_ip:'):
        ip_to_ban = data.split(':')[1]

        # Check if already banned
        existing_ban = BannedIP.query.filter_by(ip_address=ip_to_ban).first()

        if existing_ban:
            response_text = f"⚠️ L'IP {ip_to_ban} est déjà bannie."
        else:
            try:
                new_ban = BannedIP(ip_address=ip_to_ban, reason="Banned via Telegram Bot")
                db.session.add(new_ban)
                db.session.commit()
                response_text = f"✅ L'IP {ip_to_ban} a été bannie avec succès."
            except Exception as e:
                db.session.rollback()
                current_app.logger.error(f"Failed to ban IP {ip_to_ban}: {e}")
                response_text = f"❌ Erreur lors du bannissement de l'IP {ip_to_ban}."

        # Answer the callback query to stop the loading animation
        answer_url = f"https://api.telegram.org/bot{token}/answerCallbackQuery"
        requests.post(answer_url, json={
            "callback_query_id": callback_query_id,
            "text": response_text
        })

        # Send a confirmation message
        send_url = f"https://api.telegram.org/bot{token}/sendMessage"
        requests.post(send_url, json={
            "chat_id": chat_id,
            "text": response_text
        })
