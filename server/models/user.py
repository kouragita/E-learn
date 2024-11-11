from datetime import datetime
from . import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    profile = db.relationship('UserProfile', uselist=False, back_populates="user")
    role = db.relationship('Role', back_populates="users")
    learning_paths = db.relationship('UserLearningPath', back_populates="user")
    achievements = db.relationship('Achievement', back_populates="user")
    comments = db.relationship('Comment', back_populates="user")
    ratings = db.relationship('Rating', back_populates="user")
    progress = db.relationship('Progress', back_populates="user")

class UserProfile(db.Model):
    __tablename__ = 'user_profile'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    points = db.Column(db.Integer, default=0)
    xp = db.Column(db.Integer, default=0)
    bio = db.Column(db.String)
    avatar_url = db.Column(db.String)
    last_active = db.Column(db.DateTime)
    
    user = db.relationship('User', back_populates="profile")