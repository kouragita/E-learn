from flask_restful import Resource, reqparse
from app.auth.decorators import roles_required
from app.models import db
from app.models.module import Module
from app.models.learning_path import LearningPath
from app.schemas.module_schema import ModuleSchema
from app.models.learning_path import LearningPath
from app.schemas.learning_path_schema import LearningPathSchema

module_schema = ModuleSchema()
modules_schema = ModuleSchema(many=True)

learning_path_schema = LearningPathSchema()
learning_paths_schema = LearningPathSchema(many=True)

class LearningPathModulesResource(Resource):
    def get(self, path_id):
        # Fetch the learning path
        learning_path = LearningPath.query.get(path_id)
        if not learning_path:
            return {"message": "Learning Path not found"}, 404

        # Fetch all modules for this learning path, ordered by 'order'
        modules = Module.query.filter_by(learning_path_id=path_id).order_by(Module.order).all()

        # Serialize modules with the updated schema
        return modules_schema.dump(modules), 200

class LearningPathResource(Resource):
    def get(self, path_id):
        path = LearningPath.query.get(path_id)
        if not path:
            return {"message": "Learning Path not found"}, 404
        return learning_path_schema.dump(path), 200

    @roles_required(1, 2)
    def put(self, path_id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('description', type=str)
        parser.add_argument('contributor_id', type=int)
        data = parser.parse_args()

        path = LearningPath.query.get(path_id)
        if not path:
            return {"message": "Learning Path not found"}, 404
        
        path.title = data['title']
        path.description = data['description']
        path.contributor_id = data['contributor_id']
        
        db.session.commit()
        return learning_path_schema.dump(path), 200

    @roles_required(1, 2)
    def delete(self, path_id):
        path = LearningPath.query.get(path_id)
        if not path:
            return {"message": "Learning Path not found"}, 404

        db.session.delete(path)
        db.session.commit()
        return {"message": "Learning Path deleted successfully"}, 200

class LearningPathListResource(Resource):
    def get(self):
        paths = LearningPath.query.all()
        return learning_paths_schema.dump(paths), 200

    @roles_required(1, 2)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('description', type=str)
        parser.add_argument('contributor_id', type=int, required=True)
        data = parser.parse_args()

        new_path = LearningPath(
            title=data['title'],
            description=data['description'],
            contributor_id=data['contributor_id']
        )
        
        db.session.add(new_path)
        db.session.commit()
        return learning_path_schema.dump(new_path), 201
