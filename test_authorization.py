import json
import os

import pytest
from flask import Flask, jsonify

from app import app, db
from app.models import User
from app.serializer import UserSerializer


@pytest.fixture
def client():
    client = app.test_client()
    yield client

def add_user_for_test():
    if User.query.filter_by(email="testeteste1@gmail.com").first():
        db.session.delete(User.query.filter_by(email="testeteste1@gmail.com").first())
        db.session.commit()
    new_user = User(
        email= "testeteste1@gmail.com",
        password= "teste12345",
        first_name= "teste",
        last_name= "12345"
    )
    db.session.add(new_user)
    db.session.commit()

def delete_user_of_test():
    db.session.delete(User.query.filter_by(email="testeteste1@gmail.com").first())
    db.session.commit()


def test_register_user(client):
    with app.app_context():
        if User.query.filter_by(email="testeteste1@gmail.com").first():
            db.session.delete(User.query.filter_by(email="testeteste1@gmail.com").first())
            db.session.commit()
        json_data = {
            "email": "testeteste1@gmail.com",
            "password": "teste123",
            "first_name": "teste",
            "last_name": "123"
        }
        response = client.post('/api/auth/register', json=json_data, headers={"Content-Type": "application/json"})
        delete_user_of_test()
        assert response.status_code == 201
        assert response.is_json



def test_login(client):
    with app.app_context():
        add_user_for_test()
        json_data = {
           "email": "testeteste1@gmail.com",
            "password": "teste12345"
        }
        response = client.post('/api/auth/login', json=json_data, headers={"Content-Type": "application/json"})
        delete_user_of_test()
        assert response.status_code == 200
        assert (json.loads(response.get_data())['token'])
        assert response.is_json


def test_wrong_password_login(client):
    with app.app_context():
        add_user_for_test()
        json_data = {
            "email": "testeteste1@gmail.com",
            "password": "wrong_password"
        }
        response = client.post('/api/auth/login', json=json_data, headers={"Content-Type": "application/json"})
        delete_user_of_test()
        assert response.status_code == 400
        assert response.is_json


def test_user_not_register_login(client):
    with app.app_context():
        json_data = {
            "email": "user-not-registered@gmail.com",
            "password": "12345"}
        response = client.post('/api/auth/login', json=json_data, headers={"Content-Type": "application/json"})
        assert response.status_code == 400
        assert response.is_json
