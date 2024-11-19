from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)  # Ensure password hashing in practice
    email = db.Column(db.String(255), unique=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relationships
    profile = db.relationship('UserProfile', backref='user', uselist=False)
    learning_paths = db.relationship('UserLearningPath', back_populates='user')
    achievements = db.relationship('Achievement', back_populates='user')
    contributed_learning_paths = db.relationship('LearningPath', back_populates='contributor')  # Added back_populates
