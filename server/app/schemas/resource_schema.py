from marshmallow import Schema, fields

class ResourceSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    type = fields.Str()
    url = fields.Url(required=True)
    description = fields.Str()
    module_id = fields.Int(required=True)
