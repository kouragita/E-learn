from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api

# Initialize extensions
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    api = Api(app)  # Create and bind Api object here
    
    # Load configuration from config.py or another configuration file
    app.config.from_object('app.config.Config')
    
    # Initialize other extensions with the app
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    # Get allowed origins from environment variable, split by comma
    origins = os.getenv('ALLOWED_ORIGINS', 'http://localhost:3000').split(',')

    CORS(app, 
         origins=origins,
         methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
         allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
         supports_credentials=True
    )
    
    # Import models here to ensure they are known to Flask-Migrate
    from .models import (
        user, role, user_profile, learning_path, module, resource,
        quiz, comment, rating, badge, achievement, progress, user_learning_path
    )
    
    # Register all routes
    from .routes import register_routes
    from .admin import register_admin_routes
    register_routes(app, api)
    register_admin_routes(api)

    return app