from flask import Blueprint , jsonify
from flask_jwt_extended import jwt_required
from app.utils.auth import role_required
from app.utils.response import success_response , error_response
from app.models.models import User , URL

admin_bp = Blueprint("admin" , __name__)

@admin_bp.route("/api/users" , methods=["GET"])
@jwt_required()
@role_required("admin")
def get_all_users():
    url = URL.query.all()
    return jsonify([{
        "id": url.id,
        "long_url": url.long_url,
        "short_code": url.short_code,
        "created_at": url.created_at,
        "count": url.count,
        "expired_at": url.expired_at
    } for url in url]), 200

# delete user by id 



# delete all urls of a user by user id



# delete all urls 
