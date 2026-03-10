from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from app.rate_limiter.limiter import is_rate_limited


def rate_limit(limit, window):

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):

            user_id = get_jwt_identity()
            endpoint = request.endpoint

            key = f"rate_limit:user:{user_id}:{endpoint}"

            limited, retry_after = is_rate_limited(
                key,
                limit,
                window
            )

            if limited:
                return jsonify({
                    "error": "Too many requests",
                    "retry_after": retry_after
                }), 429

            return fn(*args, **kwargs)

        return wrapper
    return decorator