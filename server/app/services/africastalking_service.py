import africastalking
from flask import current_app
from app.models import db
from app.models.ussd_session import UssdSession
from .user_service import UserService

class AfricasTalkingService:
    def __init__(self):
        self.username = current_app.config['AFRICASTALKING_USERNAME']
        self.api_key = current_app.config['AFRICASTALKING_API_KEY']
        africastalking.initialize(self.username, self.api_key)
        self.sms = africastalking.SMS

    def send(self, message, recipients):
        try:
            # Ensure recipients is a list
            if not isinstance(recipients, list):
                recipients = [recipients]
            response = self.sms.send(message, recipients)
            print(f"SMS sent successfully: {response}")
            return response
        except Exception as e:
            print(f"Error sending SMS: {e}")
            raise

class UssdService:
    def __init__(self, session_id, phone_number, text):
        self.session_id = session_id
        self.phone_number = phone_number
        self.text_array = text.split('*')
        self.session = self.get_or_create_session()

    def get_or_create_session(self):
        session = UssdSession.query.filter_by(session_id=self.session_id).first()
        if not session:
            session = UssdSession(session_id=self.session_id, phone_number=self.phone_number)
            db.session.add(session)
            db.session.commit()
        return session

    def handle_request(self):
        level = len(self.text_array)
        user_input = self.text_array[-1]

        if self.session.state == 'INITIAL':
            if user_input == '1':
                self.session.state = 'REGISTER_GET_NAME'
                db.session.commit()
                return "CON Please enter your full name:"
            elif user_input == '2':
                return "END Service not yet implemented."
            else:
                return "CON Welcome to E-learn!\n1. Register\n2. Check Status"
        
        elif self.session.state == 'REGISTER_GET_NAME':
            self.session.user_data = {'name': user_input}
            self.session.state = 'REGISTER_CONFIRM'
            db.session.commit()
            return f"CON Confirm your name is {user_input}?\n1. Yes\n2. No"

        elif self.session.state == 'REGISTER_CONFIRM':
            if user_input == '1':
                try:
                    user, password = UserService.register_user_from_ussd(
                        self.phone_number,
                        self.session.user_data['name']
                    )
                    # Send SMS with credentials
                    sms_service = AfricasTalkingService()
                    message = f"Welcome to E-learn, {user.username}! Your password is {password}. Login at our website."
                    sms_service.send(message, self.phone_number)
                    
                    self.session.state = 'DONE'
                    db.session.commit()
                    return "END Thank you for registering! You will receive an SMS with your login details shortly."
                except ValueError as e:
                    self.session.state = 'DONE'
                    db.session.commit()
                    return f"END Error: {str(e)}"
                except Exception as e:
                    self.session.state = 'DONE'
                    db.session.commit()
                    return f"END An unexpected error occurred. Please try again later."
            else:
                self.session.state = 'INITIAL'
                db.session.commit()
                return self.handle_request() # Restart

        return "END An unexpected error occurred."
