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
    app.config["JWT_SECRET_KEY"] = "super-secret-key-change-me" 

    CORS(app)
    jwt.init_app(app)   
    db.init_app(app)

    from app.routes.user_routes import user_bp 
    from app.routes.auth_routes import auth_bp
    from app.services.scheduler import start_scheduler
    
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)
    
    setup_logging()
    start_scheduler(app)
    

    with app.app_context():
        db.create_all()

    return app