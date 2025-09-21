from app import db

class Module(db.Model):
    __tablename__ = 'modules'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    order_index = db.Column(db.Integer)
    learning_path_id = db.Column(db.Integer, db.ForeignKey('learning_paths.id'))
    status = db.Column(db.String(50), default='draft')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    # Relationships
    learning_path = db.relationship('LearningPath', back_populates='modules')
    resources = db.relationship('Resource', back_populates='module', cascade='all, delete-orphan')
    quizzes = db.relationship('Quiz', back_populates='module', cascade='all, delete-orphan')
    progress_records = db.relationship('Progress', back_populates='module')
