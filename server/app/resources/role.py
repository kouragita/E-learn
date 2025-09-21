from flask_restful import Resource, reqparse
from app.models import db
from app.models.role import Role
from app.schemas.role_schema import RoleSchema
from app.auth.decorators import admin_required

role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)

class RoleResource(Resource):
    method_decorators = [admin_required()]

    def get(self, role_id):
        role = Role.query.get(role_id)
        if not role:
            return {"message": "Role not found"}, 404
        return role_schema.dump(role), 200

    def put(self, role_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('description', type=str)
        data = parser.parse_args()

        role = Role.query.get(role_id)
        if not role:
            return {"message": "Role not found"}, 404

        role.name = data['name']
        role.description = data['description']
        
        db.session.commit()
        return role_schema.dump(role), 200

    def delete(self, role_id):
        role = Role.query.get(role_id)
        if not role:
            return {"message": "Role not found"}, 404

        db.session.delete(role)
        db.session.commit()
        return {"message": "Role deleted successfully"}, 200

class RoleListResource(Resource):
    method_decorators = [admin_required()]

    def get(self):
        roles = Role.query.all()
        return roles_schema.dump(roles), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('description', type=str)
        data = parser.parse_args()

        new_role = Role(
            name=data['name'],
            description=data.get('description')
        )
        
        db.session.add(new_role)
        db.session.commit()
        return role_schema.dump(new_role), 201
