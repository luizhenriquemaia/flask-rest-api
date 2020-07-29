from functools import wraps
import jwt
from flask import request, jsonify, current_app
from app.models import User


def jwt_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return jsonify({
                "error": "no token identified"
            }), 400
        try:
            decoded = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.get(decoded['id'])
        except:
            return jsonify({
                "error": "invalid token"
            }), 401
        return f(current_user=current_user, *args, **kwargs)
    return wrapper