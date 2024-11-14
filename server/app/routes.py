from flask import Blueprint
from flask_restful import Api
from app.resources.user import UserResource, UserListResource
from app.resources.role import RoleResource, RoleListResource
from app.resources.learning_path import LearningPathResource, LearningPathListResource
from app.resources.module import ModuleResource, ModuleListResource
from app.resources.resource import ResourceResource, ResourceListResource
from app.resources.quiz import QuizResource, QuizListResource
from app.resources.comment import CommentResource, CommentListResource
from app.resources.rating import RatingResource, RatingListResource
from app.resources.badge import BadgeResource, BadgeListResource
from app.resources.achievement import AchievementResource, AchievementListResource
from app.resources.progress import ProgressResource, ProgressListResource
from app.auth.auth import auth_bp  

# Initialize the API blueprint and API
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Register API resource routes
api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:id>')
api.add_resource(RoleListResource, '/roles')
api.add_resource(RoleResource, '/roles/<int:id>')
api.add_resource(LearningPathListResource, '/learning_paths')
api.add_resource(LearningPathResource, '/learning_paths/<int:id>')
api.add_resource(ModuleListResource, '/modules')
api.add_resource(ModuleResource, '/modules/<int:id>')
api.add_resource(ResourceListResource, '/resources')
api.add_resource(ResourceResource, '/resources/<int:id>')
api.add_resource(QuizListResource, '/quizzes')
api.add_resource(QuizResource, '/quizzes/<int:id>')
api.add_resource(CommentListResource, '/comments')
api.add_resource(CommentResource, '/comments/<int:id>')
api.add_resource(RatingListResource, '/ratings')
api.add_resource(RatingResource, '/ratings/<int:id>')
api.add_resource(BadgeListResource, '/badges')
api.add_resource(BadgeResource, '/badges/<int:id>')
api.add_resource(AchievementListResource, '/achievements')
api.add_resource(AchievementResource, '/achievements/<int:id>')
api.add_resource(ProgressListResource, '/progress')
api.add_resource(ProgressResource, '/progress/<int:id>')

def register_routes(app):
    # Check if the 'api' blueprint is already registered to avoid duplicates
    if 'api' not in app.blueprints:
        app.register_blueprint(api_bp, url_prefix='/api')
    
    # Register the auth blueprint for authentication-related routes with a separate prefix
    if 'auth' not in app.blueprints:
        app.register_blueprint(auth_bp, url_prefix='/auth')
