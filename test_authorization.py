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
    serializer = UserSerializer(many=False)
    data = {
        "email": "teste123@gmail.com",
        "password": "teste123",
        "first_name": "teste",
        "last_name": "123"
    }
    response = client.post('/api/auth/register', json=serializer.dump(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 201
    assert response.is_json
