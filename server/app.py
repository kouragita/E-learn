# from flask import Flask, request, jsonify
# from flask_restful import Api, Resource, reqparse
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
# from flask_migrate import Migrate
# from models.__init__ import db # Import db directly
# import os

# app = Flask(__name__)
# api = Api(app)
# CORS(app)   #cors is an online tool

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://elearndb_user:ynYdjBgjF34gfqDJgmVGHKVvDNHu2XlU@dpg-csm7n0lumphs73ck0jj0-a.oregon-postgres.render.com/elearndb'  # Example URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# migrate = Migrate(app, db)
# db.init_app(app)

# # Define a basic route
# @app.route('/')
# def home():
#     return "Hello, Render! Your Flask app is running."

# # Run the app with the appropriate port
# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5555))  # Use environment variable or default to 5555
#     app.run(host="0.0.0.0", port=port, debug=True)







from flask import Flask, request, jsonify, abort
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from models.__init__ import db
from functools import wraps
import os

# Initialize app and extensions
app = Flask(__name__)
api = Api(app)
CORS(app)   

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://elearndb_user:ynYdjBgjF34gfqDJgmVGHKVvDNHu2XlU@dpg-csm7n0lumphs73ck0jj0-a.oregon-postgres.render.com/elearndb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

# Role-based Access Control Decorator
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_role = request.headers.get("Role")  # Assume role is sent in headers
        if user_role != "Admin":
            abort(403, description="Admins only")
        return f(*args, **kwargs)
    return decorated_function

# Import Models
from models import (
    LearningPath, UserLearningPath, Module, Quiz, Resource,
    Comment, Rating, Role, User, UserProfile
)

# Helper function to serialize SQLAlchemy objects with relationships
def serialize(model_instance):
    data = {c.name: getattr(model_instance, c.name) for c in model_instance.__table__.columns}
    return data

class LearningPathResource(Resource):
    def get(self, id=None):
        if id:
            learning_path = LearningPath.query.get_or_404(id)
            response = serialize(learning_path)
            response["modules"] = [serialize(module) for module in learning_path.modules]
            response["users"] = [serialize(user_lp) for user_lp in learning_path.users]
            return jsonify(response)
        else:
            learning_paths = LearningPath.query.all()
            return jsonify([serialize(lp) for lp in learning_paths])

    def post(self):
        data = request.json
        new_learning_path = LearningPath(**data)
        db.session.add(new_learning_path)
        db.session.commit()
        return jsonify(serialize(new_learning_path)), 201

    def put(self, id):
        learning_path = LearningPath.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(learning_path, key, value)
        db.session.commit()
        return jsonify(serialize(learning_path))

    @admin_required
    def delete(self, id):
        learning_path = LearningPath.query.get_or_404(id)
        db.session.delete(learning_path)
        db.session.commit()
        return '', 204

# CRUD Resource for Module
class ModuleResource(Resource):
    def get(self, id=None):
        if id:
            module = Module.query.get_or_404(id)
            response = serialize(module)
            response["resources"] = [serialize(resource) for resource in module.resources]
            response["quizzes"] = [serialize(quiz) for quiz in module.quizzes]
            return jsonify(response)
        else:
            modules = Module.query.all()
            return jsonify([serialize(module) for module in modules])

    def post(self):
        data = request.json
        new_module = Module(**data)
        db.session.add(new_module)
        db.session.commit()
        return jsonify(serialize(new_module)), 201

    def put(self, id):
        module = Module.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(module, key, value)
        db.session.commit()
        return jsonify(serialize(module))

    @admin_required
    def delete(self, id):
        module = Module.query.get_or_404(id)
        db.session.delete(module)
        db.session.commit()
        return '', 204

# CRUD Resource for UserProfile
class UserProfileResource(Resource):
    def get(self, user_id):
        profile = UserProfile.query.get_or_404(user_id)
        return jsonify(serialize(profile))

    def post(self):
        data = request.json
        new_profile = UserProfile(**data)
        db.session.add(new_profile)
        db.session.commit()
        return jsonify(serialize(new_profile)), 201

    def put(self, user_id):
        profile = UserProfile.query.get_or_404(user_id)
        data = request.json
        for key, value in data.items():
            setattr(profile, key, value)
        db.session.commit()
        return jsonify(serialize(profile))

# CRUD Resource for Quiz
class QuizResource(Resource):
    def get(self, id=None):
        if id:
            quiz = Quiz.query.get_or_404(id)
            return jsonify(serialize(quiz))
        else:
            quizzes = Quiz.query.all()
            return jsonify([serialize(quiz) for quiz in quizzes])

    def post(self):
        data = request.json
        new_quiz = Quiz(**data)
        db.session.add(new_quiz)
        db.session.commit()
        return jsonify(serialize(new_quiz)), 201

    def put(self, id):
        quiz = Quiz.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(quiz, key, value)
        db.session.commit()
        return jsonify(serialize(quiz))

    @admin_required
    def delete(self, id):
        quiz = Quiz.query.get_or_404(id)
        db.session.delete(quiz)
        db.session.commit()
        return '', 204

# CRUD Resource for Resource
class ResourceResource(Resource):
    def get(self, id=None):
        if id:
            resource = Resource.query.get_or_404(id)
            return jsonify(serialize(resource))
        else:
            resources = Resource.query.all()
            return jsonify([serialize(resource) for resource in resources])

    def post(self):
        data = request.json
        new_resource = Resource(**data)
        db.session.add(new_resource)
        db.session.commit()
        return jsonify(serialize(new_resource)), 201

    def put(self, id):
        resource = Resource.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(resource, key, value)
        db.session.commit()
        return jsonify(serialize(resource))

    @admin_required
    def delete(self, id):
        resource = Resource.query.get_or_404(id)
        db.session.delete(resource)
        db.session.commit()
        return '', 204

# CRUD Resource for Comment
class CommentResource(Resource):
    def get(self, id=None):
        if id:
            comment = Comment.query.get_or_404(id)
            return jsonify(serialize(comment))
        else:
            comments = Comment.query.all()
            return jsonify([serialize(comment) for comment in comments])

    def post(self):
        data = request.json
        new_comment = Comment(**data)
        db.session.add(new_comment)
        db.session.commit()
        return jsonify(serialize(new_comment)), 201

    def put(self, id):
        comment = Comment.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(comment, key, value)
        db.session.commit()
        return jsonify(serialize(comment))

    @admin_required
    def delete(self, id):
        comment = Comment.query.get_or_404(id)
        db.session.delete(comment)
        db.session.commit()
        return '', 204

# CRUD Resource for Rating
class RatingResource(Resource):
    def get(self, id=None):
        if id:
            rating = Rating.query.get_or_404(id)
            return jsonify(serialize(rating))
        else:
            ratings = Rating.query.all()
            return jsonify([serialize(rating) for rating in ratings])

    def post(self):
        data = request.json
        new_rating = Rating(**data)
        db.session.add(new_rating)
        db.session.commit()
        return jsonify(serialize(new_rating)), 201

    def put(self, id):
        rating = Rating.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(rating, key, value)
        db.session.commit()
        return jsonify(serialize(rating))

    @admin_required
    def delete(self, id):
        rating = Rating.query.get_or_404(id)
        db.session.delete(rating)
        db.session.commit()
        return '', 204

# CRUD Resource for Role
class RoleResource(Resource):
    def get(self, id=None):
        if id:
            role = Role.query.get_or_404(id)
            return jsonify(serialize(role))
        else:
            roles = Role.query.all()
            return jsonify([serialize(role) for role in roles])

    def post(self):
        data = request.json
        new_role = Role(**data)
        db.session.add(new_role)
        db.session.commit()
        return jsonify(serialize(new_role)), 201

    def put(self, id):
        role = Role.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(role, key, value)
        db.session.commit()
        return jsonify(serialize(role))

    @admin_required
    def delete(self, id):
        role = Role.query.get_or_404(id)
        db.session.delete(role)
        db.session.commit()
        return '', 204

# CRUD Resource for User
class UserResource(Resource):
    def get(self, id=None):
        if id:
            user = User.query.get_or_404(id)
            return jsonify(serialize(user))
        else:
            users = User.query.all()
            return jsonify([serialize(user) for user in users])

    def post(self):
        data = request.json
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(serialize(new_user)), 201

    def put(self, id):
        user = User.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        return jsonify(serialize(user))

    @admin_required
    def delete(self, id):
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return '', 204
    
class UserLearningPathResource(Resource):
    def get(self, id=None):
        if id:
            user_learning_path = UserLearningPath.query.get_or_404(id)
            return jsonify(serialize(user_learning_path))
        else:
            user_learning_paths = UserLearningPath.query.all()
            return jsonify([serialize(user_lp) for user_lp in user_learning_paths])

    def post(self):
        data = request.json
        new_user_learning_path = UserLearningPath(**data)
        db.session.add(new_user_learning_path)
        db.session.commit()
        return jsonify(serialize(new_user_learning_path)), 201

    def put(self, id):
        user_learning_path = UserLearningPath.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(user_learning_path, key, value)
        db.session.commit()
        return jsonify(serialize(user_learning_path))

    @admin_required
    def delete(self, id):
        user_learning_path = UserLearningPath.query.get_or_404(id)
        db.session.delete(user_learning_path)
        db.session.commit()
        return '', 204

# API Endpoints
api.add_resource(UserLearningPathResource, '/user-learning-paths', '/user-learning-paths/<int:id>')
api.add_resource(LearningPathResource, '/learning-paths', '/learning-paths/<int:id>')
api.add_resource(ModuleResource, '/modules', '/modules/<int:id>')
api.add_resource(UserProfileResource, '/user-profiles/<int:user_id>')
api.add_resource(QuizResource, '/quizzes', '/quizzes/<int:id>')
api.add_resource(ResourceResource, '/resources', '/resources/<int:id>')
api.add_resource(CommentResource, '/comments', '/comments/<int:id>')
api.add_resource(RatingResource, '/ratings', '/ratings/<int:id>')
api.add_resource(RoleResource, '/roles', '/roles/<int:id>')
api.add_resource(UserResource, '/users', '/users/<int:id>')


# Custom Error Handling
@app.errorhandler(400)
def bad_request(error):
    return jsonify(error="Bad Request: Invalid or malformed input"), 400

@app.errorhandler(401)
def unauthorized(error):
    return jsonify(error="Unauthorized: Authentication required or invalid credentials"), 401

@app.errorhandler(403)
def forbidden(error):
    return jsonify(error="Forbidden: Admins only"), 403

@app.errorhandler(404)
def not_found(error):
    return jsonify(error="Resource not found"), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify(error="Internal Server Error"), 500

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5555))
    app.run(host="0.0.0.0", port=port, debug=True)
