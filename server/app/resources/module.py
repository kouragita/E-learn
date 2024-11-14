from flask_restful import Resource, reqparse
from app.models import db
from app.models.module import Module
from app.schemas.module_schema import ModuleSchema

module_schema = ModuleSchema()
modules_schema = ModuleSchema(many=True)

class ModuleResource(Resource):
    def get(self, module_id):
        module = Module.query.get(module_id)
        if not module:
            return {"message": "Module not found"}, 404
        return module_schema.dump(module), 200

    def put(self, module_id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('description', type=str)
        parser.add_argument('learning_path_id', type=int, required=True)
        parser.add_argument('order', type=int)
        data = parser.parse_args()

        module = Module.query.get(module_id)
        if not module:
            return {"message": "Module not found"}, 404

        module.title = data['title']
        module.description = data['description']
        module.learning_path_id = data['learning_path_id']
        module.order = data['order']
        
        db.session.commit()
        return module_schema.dump(module), 200

    def delete(self, module_id):
        module = Module.query.get(module_id)
        if not module:
            return {"message": "Module not found"}, 404

        db.session.delete(module)
        db.session.commit()
        return {"message": "Module deleted successfully"}, 200

class ModuleListResource(Resource):
    def get(self):
        modules = Module.query.all()
        return modules_schema.dump(modules), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('description', type=str)
        parser.add_argument('learning_path_id', type=int, required=True)
        parser.add_argument('order', type=int)
        data = parser.parse_args()

        new_module = Module(
            title=data['title'],
            description=data['description'],
            learning_path_id=data['learning_path_id'],
            order=data['order']
        )
        
        db.session.add(new_module)
        db.session.commit()
        return module_schema.dump(new_module), 201
