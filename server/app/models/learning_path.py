from app import db

class LearningPath(db.Model):
    __tablename__ = 'learning_paths'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    contributor_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relationships
    modules = db.relationship('Module', backref='learning_path', cascade='all, delete-orphan')
