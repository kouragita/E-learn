from datetime import datetime
from . import db

class Resource(db.Model):
    __tablename__ = 'resource'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    type = db.Column(db.String)
    url = db.Column(db.String)
    description = db.Column(db.Text)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'))
    
    module = db.relationship('Module', back_populates="resources")
    comments = db.relationship('Comment', back_populates="resource")
    ratings = db.relationship('Rating', back_populates="resource")
    

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', back_populates="comments")
    resource = db.relationship('Resource', back_populates="comments")
    
class Rating(db.Model):
    __tablename__ = 'rating'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', back_populates="ratings")
    resource = db.relationship('Resource', back_populates="ratings")

