from app import db

class Resource(db.Model):
    __tablename__ = 'resources'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50))
    url = db.Column(db.String(255))
    description = db.Column(db.Text)
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))
