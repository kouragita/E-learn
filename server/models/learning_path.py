from . import db

class LearningPath(db.Model):
    __tablename__ = 'learning_paths'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    contributor_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    modules = db.relationship('Module', back_populates='learning_path')
    users = db.relationship('UserLearningPath', back_populates='learning_path')


class UserLearningPath(db.Model):
    __tablename__ = 'user_learning_paths'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    learning_path_id = db.Column(db.Integer, db.ForeignKey('learning_paths.id'), primary_key=True)
    progress = db.Column(db.Integer, default=0)
    date_enrolled = db.Column(db.DateTime, default=db.func.current_timestamp())

    user = db.relationship('User', back_populates='learning_paths')
    learning_path = db.relationship('LearningPath', back_populates='users')
    

class Module(db.Model):
    __tablename__ = 'module'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    learning_path_id = db.Column(db.Integer, db.ForeignKey('learning_path.id'))
    module_order = db.Column(db.Integer)
    
    learning_path = db.relationship('LearningPath', back_populates="modules")
    resources = db.relationship('Resource', back_populates="module")
    quizzes = db.relationship('Quiz', back_populates="module")

