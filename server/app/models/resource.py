from app import db

class Resource(db.Model):
    __tablename__ = 'resources'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    type = db.Column(db.String(50), nullable=False)  # video, document, link, image
    url = db.Column(db.String(1000))  # Cloudinary URL for uploaded content
    cloudinary_public_id = db.Column(db.String(255))  # Cloudinary public ID for management
    file_size = db.Column(db.Integer)  # in bytes
    duration = db.Column(db.Integer)  # for videos, in seconds
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))
    order_index = db.Column(db.Integer)
    status = db.Column(db.String(50), default='active')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    # Relationships
    module = db.relationship('Module', back_populates='resources')
    ratings = db.relationship('Rating', back_populates='resource')
    comments = db.relationship('Comment', back_populates='resource')
