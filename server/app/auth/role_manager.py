from functools import wraps
from flask import request, jsonify
from app.models.role import Role

def check_role(required_role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_role = Role.query.get(request.headers.get('Role-ID'))
            if user_role and user_role.name == required_role:
                return f(*args, **kwargs)
            return jsonify({"message": "Permission denied"}), 403
        return decorated_function
    return decorator
