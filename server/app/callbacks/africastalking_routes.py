from flask import request
from flask_restful import Resource
from app.services.africastalking_service import UssdService

class AfricasTalkingCallback(Resource):
    def post(self):
        payload = request.form.to_dict()
        session_id = payload.get('sessionId')
        phone_number = payload.get('phoneNumber')
        text = payload.get('text')
        
        service = UssdService(session_id, phone_number, text)
        response = service.handle_request()
        return response, 200, {'Content-Type': 'text/plain'}
