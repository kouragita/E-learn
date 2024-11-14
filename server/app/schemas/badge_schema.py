from marshmallow import Schema, fields

class BadgeSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    image_url = fields.Url()
    points_required = fields.Int(required=True)
