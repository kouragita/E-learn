from .. import models
class Quiz(db.Model):
    __tablename__ = 'quiz'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    options = db.Column(db.Text)  # This could be JSON for options
    correct_answer = db.Column(db.String)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'))
    
    module = db.relationship('Module', back_populates="quizzes")