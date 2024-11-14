from marshmallow import Schema, fields

class ModuleSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    learning_path_id = fields.Int(required=True)
    order = fields.Int()
