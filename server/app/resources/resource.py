from flask_restful import Resource, reqparse
from app.models import db
from app.models.resource import Resource as ResourceModel  # Avoid naming conflict
from app.schemas.resource_schema import ResourceSchema

resource_schema = ResourceSchema()
resources_schema = ResourceSchema(many=True)

class ResourceResource(Resource):
    def get(self, resource_id):
        resource = ResourceModel.query.get(resource_id)
        if not resource:
            return {"message": "Resource not found"}, 404
        return resource_schema.dump(resource), 200

    def put(self, resource_id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('type', type=str, required=True)
        parser.add_argument('url', type=str, required=True)
        parser.add_argument('description', type=str)
        parser.add_argument('module_id', type=int, required=True)
        data = parser.parse_args()

        resource = ResourceModel.query.get(resource_id)
        if not resource:
            return {"message": "Resource not found"}, 404
        
        resource.title = data['title']
        resource.type = data['type']
        resource.url = data['url']
        resource.description = data['description']
        resource.module_id = data['module_id']
        
        db.session.commit()
        return resource_schema.dump(resource), 200

    def delete(self, resource_id):
        resource = ResourceModel.query.get(resource_id)
        if not resource:
            return {"message": "Resource not found"}, 404

        db.session.delete(resource)
        db.session.commit()
        return {"message": "Resource deleted successfully"}, 200

class ResourceListResource(Resource):
    def get(self):
        resources = ResourceModel.query.all()
        return resources_schema.dump(resources), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('type', type=str, required=True)
        parser.add_argument('url', type=str, required=True)
        parser.add_argument('description', type=str)
        parser.add_argument('module_id', type=int, required=True)
        data = parser.parse_args()

        new_resource = ResourceModel(
            title=data['title'],
            type=data['type'],
            url=data['url'],
            description=data['description'],
            module_id=data['module_id']
        )
        
        db.session.add(new_resource)
        db.session.commit()
        return resource_schema.dump(new_resource), 201
