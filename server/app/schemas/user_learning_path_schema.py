from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from flask_marshmallow import Marshmallow
from app.models.user_learning_path import UserLearningPath  
from app.models import db

class UserLearningPathSchema(SQLAlchemySchema):
    class Meta:
        model = UserLearningPath
        load_instance = True  

    user_id = auto_field()
    learning_path_id = auto_field()
    progress = auto_field()
    date_enrolled = auto_field()
    
   
