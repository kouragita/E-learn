from datetime import datetime
from . import db

class Badge(db.Model):
    __tablename__ = 'badge'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String)
    points_required = db.Column(db.Integer)
    
class Achievement(db.Model):
    __tablename__ = 'achievement'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    badge_id = db.Column(db.Integer, db.ForeignKey('badge.id'))
    date_achieved = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', back_populates="achievements")
    badge = db.relationship('Badge')