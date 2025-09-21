from app.models import db
from app.models.user import User
from werkzeug.security import generate_password_hash
import random
import string

class UserService:
    @staticmethod
    def generate_random_password(length=8):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for i in range(length))

    @staticmethod
    def register_user_from_ussd(phone_number, username):
        # Check if user already exists
        if User.query.filter_by(phone_number=phone_number).first():
            raise ValueError("Phone number already registered.")

        password = UserService.generate_random_password()
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Create a unique email and username
        base_name = username.lower().replace(' ', '.')
        email = f"{base_name}@elearn.placeholder.com"
        counter = 1
        while User.query.filter_by(email=email).first():
            email = f"{base_name}{counter}@elearn.placeholder.com"
            counter += 1
        
        new_user = User(
            username=username,
            password=hashed_password,
            email=email,
            phone_number=phone_number,
            role_id=3  # Default to Learner
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        return new_user, password
