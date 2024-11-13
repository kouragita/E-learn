from marshmallow import Schema, fields

class QuizSchema(Schema):
    id = fields.Int(dump_only=True)
    question = fields.Str(required=True)
    options = fields.List(fields.Str(), required=True)
    correct_answer = fields.Str(required=True)
    module_id = fields.Int(required=True)
