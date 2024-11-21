from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from app.models.user import User
from app import db
import jwt
import datetime

auth_bp = Blueprint('auth', __name__)

SECRET_KEY = "your_secret_key_here"

@auth_bp.route('/signup', methods=['POST'])
def signup_user():
    data = request.get_json()
    
    # Ensure required fields are present
    if not data or not data.get('username') or not data.get('password') or not data.get('email'):
        return jsonify({"message": "Username, password, and email are required"}), 400

    # Check for duplicate username or email
    existing_user = User.query.filter(
        (User.username == data['username']) | (User.email == data['email'])
    ).first()
    if existing_user:
        return jsonify({"message": "Username or email already in use"}), 409

    # Hash password
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')

    # Assign default role (Learner) if no role is provided
    new_user = User(
        username=data['username'],
        password=hashed_password,
        email=data['email'],
        role_id=3  # Default role for Learner
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201


@auth_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()

    # Validate input
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"message": "Username and password are required"}), 400

    # Retrieve user from the database
    user = User.query.filter_by(username=data['username']).first()

    if user and check_password_hash(user.password, data['password']):
        # Generate JWT token with user role and expiration
        token = jwt.encode(
            {
                "user_id": user.id,
                "role_id": user.role_id,  # Include role ID in the token
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            },
            SECRET_KEY,
            algorithm="HS256"
        )
        return jsonify({
            "message": "Login successful",
            "token": token,
            "role_id": user.role_id
        }), 200

    return jsonify({"message": "Invalid credentials"}), 401
