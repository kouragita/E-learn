from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from app.models.resource import Resource

class ResourceSchema(SQLAlchemySchema):
    class Meta:
        model = Resource
        load_instance = True
        include_fk = True

    id = auto_field(dump_only=True)
    title = auto_field(required=True)
    description = auto_field()
    type = auto_field(required=True)
    url = auto_field()
    cloudinary_public_id = auto_field()
    file_size = auto_field()
    duration = auto_field()
    order_index = auto_field()
    status = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
