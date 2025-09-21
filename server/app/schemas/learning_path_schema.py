from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from app.models.learning_path import LearningPath
from .module_schema import ModuleSchema

class LearningPathSchema(SQLAlchemySchema):
    class Meta:
        model = LearningPath
        load_instance = True
        include_fk = True

    id = auto_field(dump_only=True)
    title = auto_field(required=True)
    description = auto_field()
    category = auto_field()
    difficulty_level = auto_field()
    estimated_duration = auto_field()
    thumbnail_url = auto_field()
    status = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)

    # Nested relationships
    modules = fields.Nested(ModuleSchema, many=True, exclude=("learning_path",))
    # contributor = fields.Nested('UserSchema', only=('id', 'username'))
    # enrolled_users = fields.List(fields.Nested('UserLearningPathSchema', exclude=('learning_path',)))
