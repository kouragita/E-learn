from marshmallow import Schema, fields

class ProgressSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    module_id = fields.Int(required=True)
    completed = fields.Bool()
    completion_date = fields.DateTime()
