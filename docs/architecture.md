# Architecture du Projet

Ce document explique l'organisation des dossiers et fichiers du projet Shabaka InnovLab Platform.

## Structure des Dossiers

### `config/`
Contient les fichiers de configuration de l'application.
- `settings.py`: Contient la classe `Config` principale (chargement des variables d'environnement .env). Remplace l'ancien `config.py`.
- `database.py`: Configuration spécifique pour la base de données (si nécessaire au-delà de SQLAlchemy URI).

### `docs/`
Documentation du projet.
- `architecture.md`: Ce fichier. Explique la structure du projet.

### `lang/`
Fichiers d'internationalisation (i18n).
- `fr.json`: Fichier de traduction pour la langue française.

### `scripts/`
Scripts utilitaires pour la maintenance et l'administration.
- `create_admin.py`: Script pour créer un administrateur manuellement.
- `check_system.py`: Script pour vérifier l'intégrité du système (dossiers d'upload, permissions).

### `models/`
Modèles de base de données SQLAlchemy.
- `user.py`, `settings.py`, `forms.py`, etc.

### `routes/`
Logique des routes Flask, organisée par Blueprint.
- `public/`: Routes publiques (navigation, formulaires).
- `admin/`: Routes de l'interface d'administration.

### `services/`
Couche de service contenant la logique métier (Business Logic Layer).
- `submission_service.py`: Gestion des soumissions de formulaires.
- `notification_service.py`: Envoi de notifications (Email, Telegram).
- `file_service.py`: Gestion des uploads de fichiers.

### `statics/`
Fichiers statiques (CSS, JS, Images, Uploads).

### `templates/`
Templates Jinja2 pour le rendu HTML.

### `utils/` (Obsolète/Vide)
Ancien dossier d'utilitaires, remplacé progressivement par `services/` et `algorithms/`.

## Flux de Données
1. **Route**: Reçoit la requête HTTP.
2. **Service**: Traite la logique métier (validation, appel DB, notifications).
3. **Model**: Interagit avec la base de données.
4. **Template**: Affiche la réponse à l'utilisateur.
