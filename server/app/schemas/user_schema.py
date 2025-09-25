from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from app.models.user import User
from .role_schema import RoleSchema


class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True

    id = auto_field()
    username = auto_field()
    email = auto_field()
    phone_number = auto_field()
    created_at = auto_field()

    # Nested Relationships
    role = fields.Nested(RoleSchema, many=False)
    profile = fields.Nested('UserProfileSchema', exclude=('user_id',), many=False)
    learning_paths = fields.List(fields.Nested('UserLearningPathSchema', exclude=('user',)))
    

