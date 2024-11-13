from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(load_only=True)
    role_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
