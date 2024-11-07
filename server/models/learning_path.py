from .. import models

class LearningPath(models.Model):
    __tablename__ = 'learning_paths'
    id = db.Column(models.Integer, primary_key=True)
    title = db.Column(models.String(150), nullable=False)
    description = db.Column(models.Text)
    contributor_id = db.Column(models.Integer, models.ForeignKey('users.id'))
    created_at = db.Column(models.DateTime, default=models.func.current_timestamp())

    modules = models.relationship('Module', back_populates='learning_path')
    users = models.relationship('UserLearningPath', back_populates='learning_path')

class UserLearningPath(db.Model):
    __tablename__ = 'user_learning_path'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    learning_path_id = db.Column(db.Integer, db.ForeignKey('learning_path.id'), primary_key=True)
    progress = db.Column(db.Integer, default=0)
    date_enrolled = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', back_populates="learning_paths")
    learning_path = db.relationship('LearningPath', back_populates="users")

class Module(models.Model):
    __tablename__ = 'module'
    id = models.Column(models.Integer, primary_key=True)
    title = models.Column(models.String, nullable=False)
    description = models.Column(models.Text)
    learning_path_id = models.Column(models.Integer, models.ForeignKey('learning_path.id'))
    module_order = models.Column(models.Integer)
    
    learning_path = db.relationship('LearningPath', back_populates="modules")
    resources = db.relationship('Resource', back_populates="module")
    quizzes = db.relationship('Quiz', back_populates="module")