import re

def validate_email(email):
    """
    Validates an email address format.
    Returns True if valid, False otherwise.
    """
    if not email:
        return False
    # Simple regex for email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def validate_phone(phone):
    """
    Validates a phone number format.
    Allows for +, spaces, dashes, and digits.
    Returns True if valid, False otherwise.
    """
    if not phone:
        return False
    # Allow optional +, then digits, spaces, dashes
    pattern = r'^\+?[\d\s-]+$'
    return bool(re.match(pattern, phone))
