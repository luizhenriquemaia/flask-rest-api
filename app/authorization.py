from app import app, db
from flask import Blueprint, request, jsonify, Response
from .models import User
from .serializer import UserSerializer
import json


bp_authorization = Blueprint('authorization', __name__)


@app.route('/api/auth/register', methods=['POST'])
def register():
    serializer = UserSerializer(many=False)
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password']
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        new_user = User(
            email,
            password,
            first_name,
            last_name
        )
        #db.session.add(new_user)
        #db.session.commit()
        response_json = jsonify(
            data=serializer.dump(new_user),
            message="user added"
        )
        return response_json, 201


@app.route('/api/auth/login', methods=['POST'])
def login():
    pass