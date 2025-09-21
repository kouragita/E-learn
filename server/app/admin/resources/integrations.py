from flask_restful import Resource, reqparse
from app.models.ussd_session import UssdSession
from app.models.sms_log import SmsLog
from app.models.user import User
from app.auth.decorators import admin_required
from app.services.africastalking_service import AfricasTalkingService

class UssdLogsResource(Resource):
    method_decorators = [admin_required()]
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('per_page', type=int, default=10)
        args = parser.parse_args()

        paginated_sessions = UssdSession.query.order_by(UssdSession.created_at.desc()).paginate(
            page=args['page'], per_page=args['per_page'], error_out=False
        )
        return {
            'sessions': [s.to_dict() for s in paginated_sessions.items], # Assumes a to_dict() method
            'total': paginated_sessions.total,
            'pages': paginated_sessions.pages,
            'page': paginated_sessions.page,
        }

class SmsLogsResource(Resource):
    method_decorators = [admin_required()]
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('per_page', type=int, default=10)
        args = parser.parse_args()

        paginated_logs = SmsLog.query.order_by(SmsLog.created_at.desc()).paginate(
            page=args['page'], per_page=args['per_page'], error_out=False
        )
        return {
            'logs': [log.to_dict() for log in paginated_logs.items], # Assumes a to_dict() method
            'total': paginated_logs.total,
            'pages': paginated_logs.pages,
            'page': paginated_logs.page,
        }

class SmsBroadcastResource(Resource):
    method_decorators = [admin_required()]
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('message', type=str, required=True)
        data = parser.parse_args()

        # In a production app, this should be a background task
        users_with_phones = User.query.filter(User.phone_number.isnot(None)).all()
        recipients = [user.phone_number for user in users_with_phones]

        if not recipients:
            return {'message': 'No users with phone numbers found to send broadcast to.'}, 404

        try:
            sms_service = AfricasTalkingService()
            response = sms_service.send(data['message'], recipients)
            return {'message': f'Broadcast sent to {len(recipients)} user(s).', 'response': response}, 200
        except Exception as e:
            return {'message': 'Failed to send broadcast.', 'error': str(e)}, 500
