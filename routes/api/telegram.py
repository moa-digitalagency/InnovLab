from flask import Blueprint, request, jsonify, current_app
from models.security_logs import BannedIP
from models.settings import SiteSettings
from models import db
from services.notification_service import send_telegram_notification
import requests
import hashlib

telegram_bp = Blueprint('telegram', __name__)

@telegram_bp.route('/webhook', methods=['POST'])
def webhook():
    # Security: Verify Secret Token
    settings = SiteSettings.query.first()
    token = settings.telegram_bot_token if settings else None

    if not token:
         return jsonify({"status": "error", "message": "Configuration missing"}), 500

    expected_secret = hashlib.sha256(token.encode()).hexdigest()
    incoming_secret = request.headers.get('X-Telegram-Bot-Api-Secret-Token')

    if incoming_secret != expected_secret:
        current_app.logger.warning(f"Unauthorized Webhook Attempt. IP: {request.remote_addr}")
        return jsonify({"status": "error", "message": "Unauthorized"}), 403

    data = request.json
    if not data:
        return jsonify({'status': 'ignored'}), 200

    # Si c'est un clic sur un bouton "Bannir" (Callback Query)
    if 'callback_query' in data:
        callback = data['callback_query']
        callback_id = callback.get('id')
        callback_data = callback.get('data', '')
        # chat_id is available in callback['message']['chat']['id'] if needed,
        # but send_telegram_notification uses settings.

        if callback_data.startswith('ban_ip_'):
            ip_to_ban = callback_data.replace('ban_ip_', '')

            # Ajout à la base de données
            if not BannedIP.query.filter_by(ip_address=ip_to_ban).first():
                new_ban = BannedIP(ip_address=ip_to_ban, reason="Banni via Telegram")
                db.session.add(new_ban)
                db.session.commit()

            # UX: Stop loading spinner
            if callback_id and token:
                try:
                    answer_url = f"https://api.telegram.org/bot{token}/answerCallbackQuery"
                    requests.post(answer_url, json={
                        "callback_query_id": callback_id,
                        "text": "IP bannie avec succès"
                    }, timeout=5)
                except Exception as e:
                    current_app.logger.error(f"Failed to answer callback query: {e}")

            # Envoyer la confirmation au bot
            send_telegram_notification(f"✅ *Succès* : L'IP `{ip_to_ban}` a été définitivement bannie du site.")

    return jsonify({'status': 'success'}), 200
