from app import db
from datetime import datetime

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    points = db.Column(db.Integer, default=0)
    xp = db.Column(db.Integer, default=0)
    bio = db.Column(db.String())
    avatar_url = db.Column(db.String())
    last_active = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)