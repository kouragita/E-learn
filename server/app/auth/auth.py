from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import check_password_hash, generate_password_hash
from app.models.user import User
from app import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from datetime import datetime

from app.models.token_blocklist import TokenBlocklist

auth_bp = Blueprint('auth', __name__)

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

    # Extract optional fields
    first_name = data.get('first_name', '')
    last_name = data.get('last_name', '')
    role_name = data.get('role', 'learner') # Default to learner

    # Determine role_id and status based on role_name
    if role_name.lower() == 'contributor':
        role_id = 2  # Contributor role
        status = 'pending'
    else:
        role_id = 3  # Learner role
        status = 'active'

    new_user = User(
        username=data['username'],
        password=hashed_password,
        email=data['email'],
        role_id=role_id,
        status=status
    )
    db.session.add(new_user)
    db.session.commit()

    # Determine role name for response
    role_map = {1: "admin", 2: "contributor", 3: "student"}
    role_name = role_map.get(new_user.role_id, "student")
    
    # Generate JWT token for auto-login after signup
    additional_claims = {"role": new_user.role_id}
    token = create_access_token(identity=new_user.id, additional_claims=additional_claims)

    return jsonify({
        "message": "User created successfully",
        "token": token,
        "user": {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email,
            "role_id": new_user.role_id,
            "status": new_user.status, # Add status to response
            "role": role_name,
            "total_points": 0,
            "current_streak": 0,
            "badges": [],
            "profile_picture": None,
            "first_name": first_name,
            "last_name": last_name
        }
    }), 201


@auth_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()

    # Validate input
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"message": "Username and password are required"}), 400

    # Retrieve user from the database by username or email
    login_identifier = data.get('username')
    user = User.query.filter(
        (User.username == login_identifier) | (User.email == login_identifier)
    ).first()

    if user and check_password_hash(user.password, data['password']):
        # Generate JWT token with user role and expiration
        additional_claims = {"role": user.role_id}
        token = create_access_token(identity=user.id, additional_claims=additional_claims)
        
        # Map role_id to role name - maintaining consistency with signup
        role_map = {1: "admin", 2: "contributor", 3: "student"}
        role_name = role_map.get(user.role_id, "student")
        
        return jsonify({
            "message": "Login successful",
            "token": token,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role_id": user.role_id,
                "role": role_name,
                "total_points": 0,
                "current_streak": 0,
                "badges": [],
                "profile_picture": None
            }
        }), 200

    return jsonify({"message": "Invalid credentials"}), 401

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout_user():
    jti = get_jwt()["jti"]
    now = datetime.utcnow()
    db.session.add(TokenBlocklist(jti=jti, created_at=now))
    db.session.commit()
    return jsonify({"message": "Logout successful"}), 200