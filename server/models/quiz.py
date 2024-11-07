from .. import models

class Quiz(models.Model):
    __tablename__ = 'quiz'
    id = models.Column(models.Integer, primary_key=True)
    question = models.Column(models.Text)
    options = models.Column(models.Text)  # This could be JSON for options
    correct_answer = models.Column(models.String)
    module_id = models.Column(models.Integer, models.ForeignKey('module.id'))
    
    module = models.relationship('Module', back_populates="quizzes")