import os
import sys
import requests
import hashlib

# Add the project root to the python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from models.settings import SiteSettings

def setup_webhook():
    app = create_app()
    with app.app_context():
        settings = SiteSettings.query.first()
        if not settings or not settings.telegram_bot_token:
            print("❌ Erreur : Token Telegram introuvable dans SiteSettings.")
            return

        token = settings.telegram_bot_token
        domain = input("Entrez le nom de domaine (avec https://, ex: https://shabaka.com) : ").strip()

        if not domain.startswith('https://'):
            print("⚠️ Attention : Telegram requiert HTTPS. Assurez-vous que votre domaine est sécurisé.")

        # Generate a stateless secret token based on the bot token
        secret_token = hashlib.sha256(token.encode()).hexdigest()

        webhook_url = f"{domain}/api/telegram/webhook"
        api_url = f"https://api.telegram.org/bot{token}/setWebhook"

        print(f"Configuration du webhook vers : {webhook_url}")

        payload = {
            "url": webhook_url,
            "secret_token": secret_token
        }

        try:
            response = requests.post(api_url, json=payload)
            if response.status_code == 200 and response.json().get('ok'):
                print("✅ Webhook configuré avec succès !")
                print(f"Réponse : {response.json()}")
                print(f"🔑 Secret Token généré : {secret_token[:10]}...")
            else:
                print("❌ Échec de la configuration du webhook.")
                print(f"Réponse : {response.text}")
        except Exception as e:
            print(f"❌ Erreur lors de la requête : {e}")

if __name__ == "__main__":
    setup_webhook()
