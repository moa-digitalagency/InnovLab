# Shabaka InnovLab Platform

Plateforme institutionnelle pour l'incubateur Shabaka InnovLab.

## Fonctionnalités
- Gestion des candidatures (Startups, Fondateurs, Investisseurs)
- Admin Panel complet (Dashboard, Analytics, Paramètres SEO & Site)
- Notifications Telegram automatiques
- Gestion dynamique du Portfolio

## Installation Locale
1. Cloner le repo
2. `pip install -r requirements.txt`
3. Configurer le `.env` (voir `.env.example`)
4. Initialiser la DB : `python init_db.py`
5. Lancer : `flask run`

## Déploiement (Render/Heroku)
- Variables d'env requises : `DATABASE_URL`, `SECRET_KEY`, `ADMIN_USERNAME`, `ADMIN_PASSWORD`.
- Commande de build : `pip install -r requirements.txt`
- Commande de start : `gunicorn app:app`

## Structure
- `/models` : Base de données
- `/routes` : Logique serveur
- `/templates` : Frontend (Tailwind CSS)