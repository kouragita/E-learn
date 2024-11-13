from marshmallow import Schema, fields

class AchievementSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    badge_id = fields.Int(required=True)
    date_achieved = fields.DateTime()
