from app import db

class LearningPath(db.Model):
    __tablename__ = 'learning_paths'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=True)
    contributor_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relationships
    contributor = db.relationship('User', back_populates='contributed_learning_paths')
    enrolled_users = db.relationship('UserLearningPath', back_populates='learning_path')