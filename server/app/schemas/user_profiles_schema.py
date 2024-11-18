from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from app.models.user_profile import UserProfile  
from app.models import db
from datetime import datetime
from marshmallow import fields, Schema

class UserProfileSchema(SQLAlchemySchema):
    class Meta:
        model = UserProfile
        load_instance = True  

    user_id = auto_field()
    points = auto_field()
    xp = auto_field()
    bio = auto_field()
    avatar_url = auto_field()
    last_active = fields.DateTime(format="%Y-%m-%d")
