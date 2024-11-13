from app import db

class Module(db.Model):
    __tablename__ = 'modules'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    learning_path_id = db.Column(db.Integer, db.ForeignKey('learning_paths.id'))
    order = db.Column(db.Integer)

    # Relationships
    resources = db.relationship('Resource', backref='module', cascade='all, delete-orphan')
    quizzes = db.relationship('Quiz', backref='module', cascade='all, delete-orphan')
