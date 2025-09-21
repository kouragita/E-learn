from app import db

class Quiz(db.Model):
    __tablename__ = 'quizzes'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    options = db.Column(db.Text)  # Store JSON of options if needed
    correct_answer = db.Column(db.String(255))
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))

    # Relationships
    module = db.relationship('Module', back_populates='quizzes')
