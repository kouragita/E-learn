from .. import models

class Progress(models.Model):
    __tablename__ = 'progress'
    id = models.Column(models.Integer, primary_key=True)
    user_id = models.Column(models.Integer, models.ForeignKey('user.id'))
    module_id = models.Column(models.Integer, models.ForeignKey('module.id'))
    completed = models.Column(models.Boolean, default=False)
    completion_date = models.Column(models.DateTime)
    
    user = models.relationship('User', back_populates="progress")
    module = models.relationship('Module')