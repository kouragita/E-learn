from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash
from app.models import db
from app.models.user import User
from app.schemas.user_schema import UserSchema
from flask import jsonify

from app.auth.decorators import admin_required

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class UserResource(Resource):
    method_decorators = [admin_required()]

    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404
        return user_schema.dump(user), 200

    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        parser.add_argument('role_id', type=int, required=True)
        data = parser.parse_args()

        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404
        
        user.username = data['username']
        user.password = generate_password_hash(data['password'], method='pbkdf2:sha256')
        user.role_id = data['role_id']
        
        db.session.commit()
        return user_schema.dump(user), 200

    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404

        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted successfully"}, 200

class UserListResource(Resource):
    method_decorators = [admin_required()]

    def get(self):
        users = User.query.all()
        return users_schema.dump(users), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('role_id', type=int, required=True)
        data = parser.parse_args()

        # Check if the email is already in use
        if User.query.filter_by(email=data['email']).first():
            return {"message": "Email already in use"}, 400

        new_user = User(
            username=data['username'],
            password=generate_password_hash(data['password'], method='pbkdf2:sha256'),
            email=data['email'],
            role_id=data['role_id']
        )
        
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
