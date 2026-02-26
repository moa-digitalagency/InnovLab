from app import app
from models import db, User

with app.app_context():
    # Ensure tables exist (fix for empty DB)
    db.create_all()

    # Supprime l'ancien admin pour être sûr
    old_admin = User.query.filter_by(username='admin').first()
    if old_admin:
        db.session.delete(old_admin)
        db.session.commit()
        print("Ancien admin supprimé.")

    # Crée le nouveau
    user = User(username='admin')
    user.set_password('admin123') # Mot de passe simple pour débloquer
    db.session.add(user)
    db.session.commit()
    print("Nouvel admin créé : admin / admin123")
