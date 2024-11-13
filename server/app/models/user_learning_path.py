from app import db

class UserLearningPath(db.Model):
    __tablename__ = 'user_learning_paths'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    learning_path_id = db.Column(db.Integer, db.ForeignKey('learning_paths.id'), primary_key=True)
    progress = db.Column(db.Integer)
    date_enrolled = db.Column(db.DateTime, default=db.func.current_timestamp())

    user = db.relationship('User', back_populates='learning_paths')
    learning_path = db.relationship('LearningPath')
