from datetime import datetime
from .. import models

class Resource(models.Model):
    __tablename__ = 'resource'
    id = models.Column(models.Integer, primary_key=True)
    title = models.Column(models.String, nullable=False)
    type = models.Column(models.String)
    url = models.Column(models.String)
    description = models.Column(models.Text)
    module_id = models.Column(models.Integer, models.ForeignKey('module.id'))
    
    module = db.relationship('Module', back_populates="resources")
    comments = db.relationship('Comment', back_populates="resource")
    ratings = db.relationship('Rating', back_populates="resource")
    
class Comment(db.Model):
    __tablename__ = 'comment'
    id = models.Column(models.Integer, primary_key=True)
    content = models.Column(models.Text, nullable=False)
    user_id = models.Column(models.Integer, models.ForeignKey('user.id'))
    resource_id = models.Column(models.Integer, models.ForeignKey('resource.id'))
    created_at = models.Column(models.DateTime, default=datetime.utcnow)
    
    user = models.relationship('User', back_populates="comments")
    resource = models.relationship('Resource', back_populates="comments")
    
class Rating(models.Model):
    __tablename__ = 'rating'
    id = models.Column(models.Integer, primary_key=True)
    value = models.Column(models.Integer)
    user_id = models.Column(models.Integer, models.ForeignKey('user.id'))
    resource_id = models.Column(models.Integer, models.ForeignKey('resource.id'))
    created_at = models.Column(models.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', back_populates="ratings")
    resource = db.relationship('Resource', back_populates="ratings")
