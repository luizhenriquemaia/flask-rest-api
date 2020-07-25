import json
import os

import pytest
from flask import Flask, jsonify

from app import app, db
from app.models import Product
from app.serializer import ProductSerializer


@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_show_products(client):
    response = client.get('/api/show-products')
    assert response.status_code == 200


def test_add_product(client):
    serializer = ProductSerializer(many=False)
    data = {
        'name': 'yellow t-shirt6',
        'description': 'yellow t-shirt2 of nike',
        'price': 400.00
    }
    response = client.post('/api/product', json=serializer.dump(data), headers={"Content-Type": "application/json"})
    print(response.data)
    print(type(response.data))
    print(response.get_data(as_text=True))
    #print(dict(response.get_data(as_text=True)))
    assert response.status_code == 201
    assert response.is_json


# def test_add_product_without_json(client):
#     # bad request test
#     data = ["yellow t-shirt", "yellow t-shirt of nike", 400.00]
#     response = client.post('/api/product', json=data, headers={"Content=Type": "application/json"})
#     assert response.status_code == 400

def test_retrieve_product(client):
    response = client.get('/api/product/1')
    assert response.status_code == 200
    assert response.is_json

def test_update_product(client):
    serializer = ProductSerializer(many=False)
    data = {
        'name': 'black t-shirt',
        'description': 'black t-shirt2 of nike',
        'price': 400.12
    }
    response = client.put('/api/product/2', json=serializer.dump(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    assert response.is_json
