from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, validate
from app.models.module import Module

class ModuleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Module
        load_instance = True
        include_fk = True

    # Custom validations
    title = fields.Str(required=True, validate=validate.Length(min=1, error="Title must not be empty"))
    description = fields.Str(allow_none=True)
    learning_path_id = fields.Int(required=True, dump_only=False)
    order = fields.Int(required=True, dump_only=False)

    #  nested relationships
    resources = fields.List(fields.Nested("ResourceSchema", only=["id", "title", "url"]))
    quizzes = fields.List(fields.Nested("QuizSchema", only=["id", "question"]))
