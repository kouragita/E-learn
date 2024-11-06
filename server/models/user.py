from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    profile = db.relationship('UserProfile', uselist=False, back_populates='user')
    role = db.relationship('Role', back_populates='users')
    learning_paths = db.relationship('UserLearningPath', back_populates='user')
    comments = db.relationship('Comment', back_populates='user')
    ratings = db.relationship('Rating', back_populates='user')
    achievements = db.relationship('Achievement', back_populates='user')
    progresses = db.relationship('Progress', back_populates='user')


class UserProfile(db.Model):
    __tablename__ = 'user_profiles'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    points = db.Column(db.Integer, default=0)
    xp = db.Column(db.Integer, default=0)
    bio = db.Column(db.String(250))
    avatar_url = db.Column(db.String(250))
    last_active = db.Column(db.DateTime)

    user = db.relationship('User', back_populates='profile')
