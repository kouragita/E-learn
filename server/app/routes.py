from flask import Blueprint
from app import api
from app.resources.leaderboard import LeaderboardResource
from app.resources.userlearning_path import UserLearningPathResource, UserLearningPathListResource
from app.resources.user_profile import UserProfileResource, UserProfileListResource
from app.resources.user import UserResource, UserListResource
from app.resources.role import RoleResource, RoleListResource
from app.resources.learning_path import LearningPathResource, LearningPathListResource, LearningPathModulesResource
from app.resources.module import ModuleResource, ModuleListResource
from app.resources.resource import ResourceResource, ResourceListResource
from app.resources.quiz import QuizResource, QuizListResource
from app.resources.comment import CommentResource, CommentListResource
from app.resources.rating import RatingResource, RatingListResource
from app.resources.badge import BadgeResource, BadgeListResource
from app.resources.achievement import AchievementResource, AchievementListResource
from app.resources.progress import ProgressResource, ProgressListResource
from app.resources.profile import ProfileResource
from app.callbacks.africastalking_routes import AfricasTalkingCallback
from app.resources.ai_resources import RecommendationsResource
from app.auth.auth import auth_bp

def register_routes(app):
    # Register the auth blueprint for authentication-related routes with a separate prefix
    if 'auth' not in app.blueprints:
        app.register_blueprint(auth_bp, url_prefix='/auth')

    # Register public API resource routes
    api.add_resource(LeaderboardResource, '/api/leaderboard')
    api.add_resource(UserListResource, '/api/users')
    api.add_resource(UserResource, '/api/users/<int:user_id>')
    api.add_resource(UserProfileListResource, '/api/user-profiles')
    api.add_resource(UserProfileResource, '/api/user-profiles/<int:user_id>')
    api.add_resource(UserLearningPathListResource, '/api/user-learning-paths')
    api.add_resource(UserLearningPathResource, '/api/user-learning-paths/<int:user_id>/<int:learning_path_id>')
    api.add_resource(RoleListResource, '/api/roles')
    api.add_resource(RoleResource, '/api/roles/<int:role_id>')
    api.add_resource(LearningPathListResource, '/api/learning_paths')
    api.add_resource(LearningPathResource, '/api/learning_paths/<int:path_id>')
    api.add_resource(LearningPathModulesResource, '/api/learning_paths/<int:path_id>/modules')
    api.add_resource(ModuleListResource, '/api/modules')
    api.add_resource(ModuleResource, '/api/modules/<int:module_id>')
    api.add_resource(ResourceListResource, '/api/resources')
    api.add_resource(ResourceResource, '/api/resources/<int:resource_id>')
    api.add_resource(QuizListResource, '/api/quizzes')
    api.add_resource(QuizResource, '/api/quizzes/<int:quiz_id>')
    api.add_resource(CommentListResource, '/api/comments')
    api.add_resource(CommentResource, '/api/comments/<int:comment_id>')
    api.add_resource(RatingListResource, '/api/ratings')
    api.add_resource(RatingResource, '/api/ratings/<int:rating_id>')
    api.add_resource(BadgeListResource, '/api/badges')
    api.add_resource(BadgeResource, '/api/badges/<int:badge_id>')
    api.add_resource(AchievementListResource, '/api/achievements')
    api.add_resource(AchievementResource, '/api/achievements/<int:id>')
    api.add_resource(ProgressListResource, '/api/progress')
    api.add_resource(ProgressResource, '/api/progress/<int:progress_id>')
    api.add_resource(ProfileResource, '/api/profile')
    api.add_resource(AfricasTalkingCallback, '/api/callbacks/africas-talking')
    api.add_resource(RecommendationsResource, '/api/ai/recommendations')        