import random
import string
import re
from werkzeug.security import generate_password_hash, check_password_hash

RESERVED = {"admin", "api", "users"}

from app.utils.response import error_response

def generate_short_code(length=6):
    
    """Generates a random short code of specified length."""

    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def hash_password(password):
    """Hashes a password using Werkzeug's security utilities."""
    return generate_password_hash(password)

def verify_password(stored_password, provided_password):
    """Verifies a provided password against the stored hashed password."""
    return check_password_hash(stored_password, provided_password)

def is_valid_url(short_code):
    """Validates if the provided string is a valid URL."""
    if short_code in RESERVED:
        return False
    
    return re.match("^[a-zA-Z0-9_-]{3,20}$", short_code)