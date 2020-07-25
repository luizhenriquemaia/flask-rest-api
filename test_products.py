from flask import Flask, jsonify
from app import app, db
from app.models import Product
from app.serializer import ProductSerializer
import os
import pytest
import json


@pytest.fixture
def client():
    client = app.test_client()
    yield client



def test_show_products(client):
    response = client.get('/api/show-products')
    assert response.status_code == 200
    #assert response.status_code == 204


def test_add_product(client):
    serializer = ProductSerializer(many=False)
    data = {
        'name': 'yellow t-shirt3',
        'description': 'yellow t-shirt2 of nike',
        'price': 400.00
    }
    
    db.session.flush()
    response = client.post('/api/product', json=serializer.dump(data), headers={"Content-Type": "application/json"})
    db.session.rollback()
    assert response.status_code == 201


# def test_add_product_without_json(client):
#     # bad request test
#     data = ["yellow t-shirt", "yellow t-shirt of nike", 400.00]
#     response = client.post('/api/product', json=data, headers={"Content=Type": "application/json"})
#     assert response.status_code == 400