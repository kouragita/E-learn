from . import db

class Quiz(db.Model):
    __tablename__ = 'quiz'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)  
    options = db.Column(db.JSON, nullable=True)  
    correct_answer = db.Column(db.String(), nullable=False)  
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=True)  
    
    module = db.relationship('Module', back_populates="quizzes")