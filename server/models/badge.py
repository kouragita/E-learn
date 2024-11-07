from datetime import datetime
from .. import models

class Badge(models.Model):
    __tablename__ = 'badge'
    id = models.Column(models.Integer, primary_key=True)
    name = models.Column(models.String, nullable=False)
    description = models.Column(models.Text)
    image_url = models.Column(models.String)
    points_required = models.Column(models.Integer)
    
class Achievement(models.Model):
    __tablename__ = 'achievement'
    id = models.Column(models.Integer, primary_key=True)
    user_id = models.Column(models.Integer, models.ForeignKey('user.id'))
    badge_id = models.Column(models.Integer, models.ForeignKey('badge.id'))
    date_achieved = models.Column(models.DateTime, default=datetime.utcnow)
    
    user = models.relationship('User', back_populates="achievements")
    badge = models.relationship('Badge')