from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS

# Initialize extensions
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Load configuration from config.py or another configuration file
    app.config.from_object('app.config.Config')
    
    # Initialize extensions with the app
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db) 
    CORS(app, origins=[
        "https://new-crowdsourced.onrender.com",
        "http://localhost:3000"  # For development
    ])
    
    # Import models here to register them with SQLAlchemy
    with app.app_context():
        from .models import (
            user, role, user_profile, learning_path, module, resource,
            quiz, comment, rating, badge, achievement, progress, user_learning_path
        )
        db.create_all()  # Create tables for all models
    
    # Import and register your blueprints or APIs here
    from .routes import register_routes
    register_routes(app)  # Register main API routes and auth routes

    return app