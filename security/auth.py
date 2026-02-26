from models import User

def load_user(user_id):
    """
    Callback for Flask-Login to load user by ID.
    Used by login_manager.user_loader in app.py.
    """
    return User.query.get(int(user_id))

def verify_user_credentials(username, password):
    """
    Verifies username and password against the database.
    Returns the user object if valid, None otherwise.
    """
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
    return None
