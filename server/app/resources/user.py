from flask_restful import Resource, reqparse
from app.models import db
from app.models.user import User
from app.schemas.user_schema import UserSchema
from flask import jsonify

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class UserResource(Resource):
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
        user.password = data['password']  # Consider hashing passwords in practice
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
            password=data['password'],  # Consider hashing passwords in practice
            email=data['email'],
            role_id=data['role_id']
        )
        
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
