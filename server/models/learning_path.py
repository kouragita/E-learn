from . import db

class LearningPath(db.Model):
    __tablename__ = 'learning_paths'
    id = db.Column(models.Integer, primary_key=True)
    title = db.Column(models.String(150), nullable=False)
    description = db.Column(models.Text)
    contributor_id = db.Column(models.Integer, models.ForeignKey('users.id'))
    created_at = db.Column(models.DateTime, default=models.func.current_timestamp())

    modules = db.relationship('Module', back_populates='learning_path')
    users = db.relationship('UserLearningPath', back_populates='learning_path')


class UserLearningPath(db.Model):
    __tablename__ = 'user_learning_paths'
    user_id = models.Column(models.Integer, models.ForeignKey('users.id'), primary_key=True)
    learning_path_id = models.Column(models.Integer, models.ForeignKey('learning_paths.id'), primary_key=True)
    progress = models.Column(models.Integer, default=0)
    date_enrolled = models.Column(models.DateTime, default=models.func.current_timestamp())

    user = models.relationship('User', back_populates='learning_paths')
    learning_path = models.relationship('LearningPath', back_populates='users')
    

class Module(models.Model):
    __tablename__ = 'module'
    id = models.Column(models.Integer, primary_key=True)
    title = models.Column(models.String, nullable=False)
    description = models.Column(models.Text)
    learning_path_id = models.Column(models.Integer, db.ForeignKey('learning_path.id'))
    module_order = models.Column(models.Integer)
    
    learning_path = models.relationship('LearningPath', back_populates="modules")
    resources = models.relationship('Resource', back_populates="module")
    quizzes = models.relationship('Quiz', back_populates="module")

