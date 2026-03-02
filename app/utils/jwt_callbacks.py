from flask_jwt_extended import JWTManager
from app.models.models import User  

def register_jwt_callbacks(jwt : JWTManager):
    @jwt.user_lookup_loader
    def load_user(jwt_header, jwt_data):
        identity = jwt_data["sub"]
        user = User.query.get(int(identity))
        return user