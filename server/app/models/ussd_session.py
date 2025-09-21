from app import db

class UssdSession(db.Model):
    __tablename__ = 'ussd_sessions'

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(100), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    state = db.Column(db.String(50), default='INITIAL')
    user_data = db.Column(db.JSON, default={})
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def to_dict(self):
        return {
            'id': self.id,
            'session_id': self.session_id,
            'phone_number': self.phone_number,
            'state': self.state,
            'user_data': self.user_data,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
