from flask import Flask
from app import app
import os
import pytest


@pytest.fixture
def client():
    client = app.test_client()
    yield client



def test_show_products(client):
    response = client.get('/show-products')
    assert response.status_code == 204