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


def test_register_user(client):
    with app.app_context():
        json_data = {
            "email": "teste123@gmail.com",
            "password": "teste123",
            "first_name": "teste",
            "last_name": "123"
        }
        response = client.post('/api/auth/register', json=json_data, headers={"Content-Type": "application/json"})
        assert response.status_code == 201
        assert response.is_json


def test_login(client):
    with app.app_context():
        json_data = {
            "email": "luizhenriquembh@gmail.com",
            "password": "12345"}
        response = client.post('/api/auth/login', json=json_data, headers={"Content-Type": "application/json"})
        assert response.status_code == 200
        assert response.is_json

def test_wrong_password_login(client):
    with app.app_context():
        json_data = {
            "email": "luizhenriquembh@gmail.com",
            "password": "wrong_password"}
        response = client.post('/api/auth/login', json=json_data, headers={"Content-Type": "application/json"})
        assert response.status_code == 403
        assert response.is_json


def test_user_not_register_login(client):
    with app.app_context():
        json_data = {
            "email": "user-not-registered@gmail.com",
            "password": "12345"}
        response = client.post('/api/auth/login', json=json_data, headers={"Content-Type": "application/json"})
        assert response.status_code == 404
        assert response.is_json
