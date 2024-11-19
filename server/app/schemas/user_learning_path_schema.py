from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from flask_marshmallow import Marshmallow
from app.models.user_learning_path import UserLearningPath  
from app.models import db
from marshmallow import fields

class UserLearningPathSchema(SQLAlchemySchema):
    class Meta:
        model = UserLearningPath
        include_relationships = True
        load_instance = True
        

    user_id = auto_field()
    learning_path_id = auto_field()
    progress = auto_field()
    date_enrolled = auto_field()

    # Add learning_path for nested serialization
    learning_path = fields.Nested('LearningPathSchema', only=('id', 'title'))
    user = fields.Nested('UserSchema')  # Adjust based on your UserSchema


