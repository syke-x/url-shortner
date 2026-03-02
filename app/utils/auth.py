from flask_jwt_extended import verify_jwt_in_request , get_jwt
from functools import wraps
from flask import jsonify

def role_required(required_role):
    def wrapper(f):
        @wraps(f)
        def decorator(*args , **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            user_role = claims.get("role", "user")

            if user_role != required_role:
                return jsonify({"msg": "Forbidden: Insufficient permissions"}), 403

            return f(*args, **kwargs)
        
        return decorator
    return wrapper
