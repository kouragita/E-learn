from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt

def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims.get("role") != 1:
                return jsonify(msg="Admins only!"), 403
            else:
                return fn(*args, **kwargs)
        return decorator
    return wrapper

def roles_required(*roles):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims.get("role") not in roles:
                return jsonify(msg="Access denied!"), 403
            else:
                return fn(*args, **kwargs)
        return decorator
    return wrapper
