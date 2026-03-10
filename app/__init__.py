from datetime import timedelta
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from app.logging_config import setup_logging




db = SQLAlchemy()
jwt = JWTManager()
def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["JWT_SECRET_KEY"] = "a_very_long_random_secret_key_for_jwt_security_12345"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)

    CORS(app)
    jwt.init_app(app)   
    db.init_app(app)

    from app.routes.user_routes import user_bp 
    from app.routes.auth_routes import auth_bp
    from app.services.scheduler import start_scheduler
    from app.utils.jwt_callbacks import register_jwt_callbacks
    
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)
    register_jwt_callbacks(jwt)
    
    setup_logging()
    start_scheduler(app)
    

    with app.app_context():
        db.create_all()

    return app