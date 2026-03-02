from flask import Blueprint, request, jsonify , redirect
import random 
import string

from flask_jwt_extended import jwt_required
from app.models.models import URL 
from app.services.url_service import create_short_url , create_custom_short_url
from app.utils.auth import role_required
from app.utils.response import success_response , error_response
from app.services.redirect_url import get_and_redirect_url
from app import db

user_bp = Blueprint("main" , __name__)


@user_bp.route("/api/users", methods=["GET"])
@jwt_required()
@role_required("admin")
def get_users():
    all_urls = URL.query.all()
    return jsonify([{
        "id": url.id,
        "long_url": url.long_url,
        "short_code": url.short_code,
        "created_at": url.created_at,
        "count": url.count,
        "expired_at": url.expired_at
    } for url in all_urls]), 200

@user_bp.route("/api/shorten", methods=["POST"])
def add_user():
    
    data = request.get_json()

    if not data or "long_url" not in data:
        return error_response("Invalid request body", 400)

    long_url = data["long_url"]
    custom_short_code = data.get("custom_short_code")
    ttl_seconds = data.get("ttl_seconds" , 30)



    if custom_short_code:
        return create_custom_short_url(long_url, custom_short_code, ttl_seconds)


    if not data or "long_url" not in data:
        return error_response("Invalid request body", 400)

    
    
    return create_short_url(long_url , ttl_seconds)
    

@user_bp.route("/api/users/<short_code>", methods=["GET"])
def redirect_url(short_code):
    return get_and_redirect_url(short_code)