from app import db

class Achievement(db.Model):
    __tablename__ = 'achievements'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    badge_id = db.Column(db.Integer, db.ForeignKey('badges.id'))
    date_achieved = db.Column(db.DateTime, default=db.func.current_timestamp())

    user = db.relationship('User', back_populates='achievements')