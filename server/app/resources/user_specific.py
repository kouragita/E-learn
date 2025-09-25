from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User, LearningPath, UserLearningPath
from app.schemas.learning_path_schema import LearningPathSchema

learning_path_schema = LearningPathSchema(many=True)

class EnrolledPathsResource(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404

        enrolled_paths = [ulp.learning_path for ulp in user.learning_paths]
        return learning_path_schema.dump(enrolled_paths), 200

class AuthoredPathsResource(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404

        authored_paths = user.contributed_learning_paths
        return learning_path_schema.dump(authored_paths), 200
