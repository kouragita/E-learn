from .. import models

class User(models.Model):
    __tablename__ = 'users'
    id = models.Column(models.Integer, primary_key=True)
    username = models.Column(models.String(80), unique=True, nullable=False)
    password = models.Column(models.String(120), nullable=False)
    role_id = models.Column(models.Integer, models.ForeignKey('roles.id'), nullable=False)
    created_at = models.Column(models.DateTime, default=models.func.current_timestamp())

    profile = models.relationship('UserProfile', uselist=False, back_populates='user')
    role = models.relationship('Role', back_populates='users')
    learning_paths = models.relationship('UserLearningPath', back_populates='user')
    comments = models.relationship('Comment', back_populates='user')
    ratings = models.relationship('Rating', back_populates='user')
    achievements = models.relationship('Achievement', back_populates='user')
    progresses = models.relationship('Progress', back_populates='user')


class UserProfile(models.Model):
    __tablename__ = 'user_profiles'
    user_id = models.Column(models.Integer, models.ForeignKey('users.id'), primary_key=True)
    points = models.Column(models.Integer, default=0)
    xp = models.Column(models.Integer, default=0)
    bio = models.Column(models.String(250))
    avatar_url = models.Column(models.String(250))
    last_active = models.Column(models.DateTime)

    user = models.relationship('User', back_populates='profile')
