from app import db

class Rating(db.Model):
    __tablename__ = 'ratings'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    resource_id = db.Column(db.Integer, db.ForeignKey('resources.id'))
    learning_path_id = db.Column(db.Integer, db.ForeignKey('learning_paths.id'))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relationships
    learning_path = db.relationship('LearningPath', back_populates='ratings')
    resource = db.relationship('Resource', back_populates='ratings')
