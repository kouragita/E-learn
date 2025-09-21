from app import db

class LearningPath(db.Model):
    __tablename__ = 'learning_paths'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(100))
    difficulty_level = db.Column(db.String(50))  # beginner, intermediate, advanced
    estimated_duration = db.Column(db.Integer)  # in minutes
    thumbnail_url = db.Column(db.String(500))
    contributor_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.String(50), default='draft')  # draft, published, archived
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    # Relationships
    contributor = db.relationship('User', back_populates='contributed_learning_paths')
    modules = db.relationship('Module', back_populates='learning_path', cascade='all, delete-orphan')
    enrolled_users = db.relationship('UserLearningPath', back_populates='learning_path')
    ratings = db.relationship('Rating', back_populates='learning_path')