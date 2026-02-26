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

    if User.query.filter_by(username=username,password=password).first():
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200 
    
    return jsonify({"msg": "Bad username or password"}), 401

@auth_bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return error_response("Username and password are required", 400)
    
    hashed_password = hash_password(password)

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already exists"}), 400

    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201