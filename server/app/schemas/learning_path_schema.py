from marshmallow import Schema, fields

class LearningPathSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    contributor_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
