from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from app.models.module import Module
from .resource_schema import ResourceSchema

class ModuleSchema(SQLAlchemySchema):
    class Meta:
        model = Module
        load_instance = True
        include_fk = True

    id = auto_field(dump_only=True)
    title = auto_field(required=True)
    description = auto_field()
    order_index = auto_field()
    status = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)

    # Nested relationships
    resources = fields.Nested(ResourceSchema, many=True, exclude=("module",))
    # quizzes = fields.List(fields.Nested("QuizSchema", only=["id", "question"]))
