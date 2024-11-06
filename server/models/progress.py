from . import db

class Progress(db.Model):
    __tablename__ = 'progress'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'))
    completed = db.Column(db.Boolean, default=False)
    completion_date = db.Column(db.DateTime)
    
    user = db.relationship('User', back_populates="progress")
    module = db.relationship('Module')