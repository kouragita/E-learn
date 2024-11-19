from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from app.models.learning_path import LearningPath  # Ensure this import is correct

class LearningPathSchema(SQLAlchemySchema):
    class Meta:
        model = LearningPath  # Correct reference to the `LearningPath` model
        load_instance = True

    id = auto_field(dump_only=True)
    title = auto_field(required=True)
    description = auto_field()
    contributor_id = auto_field(required=True)
    created_at = auto_field(dump_only=True)

    # Nested relationships
    contributor = fields.Nested('UserSchema', only=('id', 'username'))
    enrolled_users = fields.List(fields.Nested('UserLearningPathSchema', exclude=('learning_path',)))
