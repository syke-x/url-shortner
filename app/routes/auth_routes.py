from flask_jwt_extended import create_access_token
from flask import Blueprint, request, jsonify
from app.utils.utils import hash_password, verify_password 
from app.utils.response import success_response , error_response
from app.models.models import User 
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user =  User.query.filter_by(username=username).first()

    if not user or not verify_password(user.hashed_password, password):
        return error_response("Invalid username or password", 401)

    access_token = create_access_token(
        identity=str(user.user_id),
        additional_claims= {
            "role" : user.role 
        }

    )

    return success_response(data={"access_token": access_token}, message="Login successful", status_code=200)
                            
@auth_bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    if not username or not password:
        return error_response("Username and password are required", 400)
    
    hashed_password = hash_password(password)

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already exists"}), 400

    new_user = User(username=username, hashed_password=hashed_password , role=role)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201