from marshmallow import Schema, fields

class RatingSchema(Schema):
    id = fields.Int(dump_only=True)
    value = fields.Int(required=True)
    user_id = fields.Int(required=True)
    resource_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
