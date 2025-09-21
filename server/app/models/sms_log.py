from app import db

class SmsLog(db.Model):
    __tablename__ = 'sms_logs'

    id = db.Column(db.Integer, primary_key=True)
    to_number = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    message_id = db.Column(db.String(100), nullable=True)
    cost = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        return {
            'id': self.id,
            'to_number': self.to_number,
            'message': self.message,
            'status': self.status,
            'message_id': self.message_id,
            'cost': self.cost,
            'created_at': self.created_at.isoformat(),
        }
