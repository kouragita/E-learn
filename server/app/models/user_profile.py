from app import db

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    points = db.Column(db.Integer, default=0)
    xp = db.Column(db.Integer, default=0)
    bio = db.Column(db.String(255))
    avatar_url = db.Column(db.String(255))
    last_active = db.Column(db.DateTime)
