from flask_restful import Resource, reqparse
from app.models import db
from app.models.user_learning_path import UserLearningPath
from app.schemas.user_learning_path_schema import UserLearningPathSchema
from flask import jsonify

# Initialize schema instances
user_learning_path_schema = UserLearningPathSchema()
user_learning_paths_schema = UserLearningPathSchema(many=True)

class UserLearningPathResource(Resource):
    def get(self, user_id, learning_path_id):
        user_learning_path = UserLearningPath.query.filter_by(user_id=user_id, learning_path_id=learning_path_id).first()
        if not user_learning_path:
            return {"message": "User learning path not found"}, 404
        return user_learning_path_schema.dump(user_learning_path), 200

    def put(self, user_id, learning_path_id):
        parser = reqparse.RequestParser()
        parser.add_argument('progress', type=int, required=False)
        data = parser.parse_args()

        user_learning_path = UserLearningPath.query.filter_by(user_id=user_id, learning_path_id=learning_path_id).first()
        if not user_learning_path:
            return {"message": "User learning path not found"}, 404

        # Update fields if provided
        if data['progress'] is not None:
            user_learning_path.progress = data['progress']

        db.session.commit()
        return user_learning_path_schema.dump(user_learning_path), 200

    def delete(self, user_id, learning_path_id):
        user_learning_path = UserLearningPath.query.filter_by(user_id=user_id, learning_path_id=learning_path_id).first()
        if not user_learning_path:
            return {"message": "User learning path not found"}, 404

        db.session.delete(user_learning_path)
        db.session.commit()
        return {"message": "User learning path deleted successfully"}, 200

class UserLearningPathListResource(Resource):
    def get(self):
        user_learning_paths = UserLearningPath.query.all()
        return user_learning_paths_schema.dump(user_learning_paths), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True)
        parser.add_argument('learning_path_id', type=int, required=True)
        parser.add_argument('progress', type=int, required=False, default=0)
        data = parser.parse_args()

        # Check if the user learning path already exists
        if UserLearningPath.query.filter_by(user_id=data['user_id'], learning_path_id=data['learning_path_id']).first():
            return {"message": "User learning path already exists"}, 409

        new_user_learning_path = UserLearningPath(
            user_id=data['user_id'],
            learning_path_id=data['learning_path_id'],
            progress=data['progress']
        )

        db.session.add(new_user_learning_path)
        db.session.commit()
        return user_learning_path_schema.dump(new_user_learning_path), 201
