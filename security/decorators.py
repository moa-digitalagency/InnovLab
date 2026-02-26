from functools import wraps
from flask import abort, redirect, url_for
from flask_login import current_user

def admin_required(f):
    """
    Decorator to ensure the current user is an administrator.
    Checks if user is authenticated and if user ID is 1.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('auth.login'))

        # Check if user is the main admin (ID 1)
        if current_user.id != 1:
            abort(403)

        return f(*args, **kwargs)
    return decorated_function
