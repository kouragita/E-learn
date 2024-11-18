from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from app.models.user import User  

class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True  

    id = auto_field()
    username = auto_field()
    email = auto_field()
    role_id = auto_field()
    created_at = auto_field()

    # Nested relationships
    profile = fields.Nested('UserProfileSchema', exclude=('user_id',), many=False)
    learning_paths = fields.List(fields.Nested('UserLearningPathSchema', exclude=('user',)))
    achievements = fields.List(fields.Nested('AchievementSchema', exclude=('user',)))

    

