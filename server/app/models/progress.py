from app import db

class Progress(db.Model):
    __tablename__ = 'progress'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))
    completed = db.Column(db.Boolean, default=False)
    completion_date = db.Column(db.DateTime)

    # Relationships
    module = db.relationship('Module', back_populates='progress_records')
