from flask_restful import Resource, reqparse
from flask import request, jsonify, current_app
from app.models import db
from app.models.learning_path import LearningPath
from app.models.module import Module
from app.models.resource import Resource
from app.schemas.learning_path_schema import LearningPathSchema
from app.schemas.module_schema import ModuleSchema
from app.schemas.resource_schema import ResourceSchema
from app.auth.decorators import admin_required
from app.services.cloudinary_service import CloudinaryService

# Schemas
learning_path_schema = LearningPathSchema()
learning_paths_schema = LearningPathSchema(many=True)
module_schema = ModuleSchema()
modules_schema = ModuleSchema(many=True)
resource_schema = ResourceSchema()
resources_schema = ResourceSchema(many=True)

# Learning Path Resources
class AdminLearningPathListResource(Resource):
    method_decorators = [admin_required()]
    def get(self):
        paths = LearningPath.query.all()
        return learning_paths_schema.dump(paths), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('description', type=str)
        parser.add_argument('category', type=str)
        parser.add_argument('difficulty_level', type=str)
        data = parser.parse_args()
        new_path = LearningPath(**data)
        db.session.add(new_path)
        db.session.commit()
        return learning_path_schema.dump(new_path), 201

class AdminLearningPathResource(Resource):
    method_decorators = [admin_required()]
    def get(self, path_id):
        path = LearningPath.query.get_or_404(path_id)
        return learning_path_schema.dump(path)

    def put(self, path_id):
        path = LearningPath.query.get_or_404(path_id)
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('status', type=str)
        data = parser.parse_args()
        for key, value in data.items():
            if value is not None:
                setattr(path, key, value)
        db.session.commit()
        return learning_path_schema.dump(path)

    def delete(self, path_id):
        path = LearningPath.query.get_or_404(path_id)
        db.session.delete(path)
        db.session.commit()
        return {'message': 'Learning Path deleted'}, 200

# Module Resources
class AdminModuleListResource(Resource):
    method_decorators = [admin_required()]
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('learning_path_id', type=int, required=True)
        data = parser.parse_args()
        new_module = Module(**data)
        db.session.add(new_module)
        db.session.commit()
        return module_schema.dump(new_module), 201

class AdminModuleResource(Resource):
    method_decorators = [admin_required()]
    def put(self, module_id):
        module = Module.query.get_or_404(module_id)
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('status', type=str)
        data = parser.parse_args()
        for key, value in data.items():
            if value is not None:
                setattr(module, key, value)
        db.session.commit()
        return module_schema.dump(module)

    def delete(self, module_id):
        module = Module.query.get_or_404(module_id)
        db.session.delete(module)
        db.session.commit()
        return {'message': 'Module deleted'}, 200

# Resource Resources
class AdminResourceListResource(Resource):
    method_decorators = [admin_required()]
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('module_id', type=int, required=True)
        parser.add_argument('type', type=str, required=True)
        parser.add_argument('file_url', type=str)
        args = parser.parse_args()
        
        cloudinary_result = None
        if 'file' in request.files:
            file = request.files['file']
            folder = f"elearn/modules/{args.module_id}/resources"
            cloudinary_result = CloudinaryService.upload_file(file, folder=folder)
        
        resource = Resource(
            title=args.title,
            module_id=args.module_id,
            type=args.type,
            url=cloudinary_result['secure_url'] if cloudinary_result else args.file_url,
            cloudinary_public_id=cloudinary_result['public_id'] if cloudinary_result else None,
            file_size=cloudinary_result.get('bytes', 0) if cloudinary_result else 0
        )
        db.session.add(resource)
        db.session.commit()
        return resource_schema.dump(resource), 201

class AdminLearningPathModulesResource(Resource):
    method_decorators = [admin_required()]
    def get(self, path_id):
        learning_path = LearningPath.query.get_or_404(path_id)
        return modules_schema.dump(learning_path.modules)

class AdminModuleResourcesResource(Resource):
    method_decorators = [admin_required()]
    def get(self, module_id):
        module = Module.query.get_or_404(module_id)
        return resources_schema.dump(module.resources)

class AdminResourceResource(Resource):
    method_decorators = [admin_required()]
    def delete(self, resource_id):
        resource = Resource.query.get_or_404(resource_id)
        if resource.cloudinary_public_id:
            try:
                CloudinaryService.delete_file(resource.cloudinary_public_id, resource.type)
            except Exception as e:
                current_app.logger.error(f"Failed to delete from Cloudinary: {str(e)}")
        
        db.session.delete(resource)
        db.session.commit()
        return {'message': 'Resource deleted'}, 200

