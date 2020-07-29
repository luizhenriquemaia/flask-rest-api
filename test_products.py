import json
import os

import pytest
from flask import Flask, jsonify

from app import app, db
from app.models import Product, User


@pytest.fixture
def client():
    client = app.test_client()
    yield client


def add_product_for_test():
    if Product.query.filter_by(name="product_test_1").first():
        db.session.delete(Product.query.filter_by(name="product_test_1").first())
        db.session.commit()
    new_product = Product(
        name="product_test_1", 
        description="a register for tests only", 
        price=123.33
    )
    db.session.add(new_product)
    db.session.commit()

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
    return (new_user)


def login_user_for_test(user, client):
    json_data = {
        "email": "testeteste1@gmail.com",
        "password": "teste12345"
    }
    response = client.post('/api/auth/login', json=json_data, headers={"Content-Type": "application/json"})
    return json.loads(response.get_data())['token']
    

def delete_product_of_test():
    if Product.query.filter_by(name="product_test_1").first():
        db.session.delete(Product.query.filter_by(name="product_test_1").first())
        db.session.commit()


def delete_user_of_test():
    if User.query.filter_by(email="testeteste1@gmail.com").first():
        db.session.delete(User.query.filter_by(email="testeteste1@gmail.com").first())
        db.session.commit()


############### test functions ###############
def test_show_products(client):
    with app.app_context():
        new_user = add_user_for_test()
        token = login_user_for_test(new_user, client)
        add_product_for_test()
        response = client.get('/api/show-products', headers={"Authorization": token})
        delete_product_of_test()
        delete_user_of_test()
        assert response.status_code == 200


def test_show_products_without_token(client):
    with app.app_context():
        add_product_for_test()
        response = client.get('/api/show-products')
        delete_product_of_test()
        assert response.status_code == 400


def test_add_product(client):
    with app.app_context():
        new_user = add_user_for_test()
        token = login_user_for_test(new_user, client)
        delete_product_of_test()
        json_data = {
            'name': 'product_test_1',
            'description': 'a register for tests only',
            'price': 123.33
        }
        response = client.post('/api/product', json=json_data, headers={
            "Content-Type": "application/json", "Authorization": token
        })
        delete_product_of_test()
        delete_user_of_test()
        assert response.status_code == 201
        assert json.loads(response.get_data())['data']
        assert json.loads(response.get_data())['message'], "created"
        assert response.is_json


def test_add_product_without_token(client):
    with app.app_context():
        delete_product_of_test()
        json_data = {
            'name': 'product_test_1',
            'description': 'a register for tests only',
            'price': 123.33
        }
        response = client.post('/api/product', json=json_data, headers={
            "Content-Type": "application/json"
        })
        delete_product_of_test()
        assert response.status_code == 400
        assert response.is_json


def test_retrieve_product(client):
    with app.app_context():
        new_user = add_user_for_test()
        token = login_user_for_test(new_user, client)
        add_product_for_test()
        id_product = Product.query.filter_by(name="product_test_1").first().id
        response = client.get(f'/api/product/{id_product}', headers={
            "Authorization": token
        })
        delete_product_of_test()
        delete_user_of_test()
        assert response.status_code == 200
        assert json.loads(response.get_data())['data']
        assert response.is_json


def test_retrieve_product_without_token(client):
    with app.app_context():
        add_product_for_test()
        id_product = Product.query.filter_by(name="product_test_1").first().id
        response = client.get(f'/api/product/{id_product}')
        delete_product_of_test()
        assert response.status_code == 400
        assert response.is_json


def test_retrieve_product_that_dont_exists(client):
    with app.app_context():
        new_user = add_user_for_test()
        token = login_user_for_test(new_user, client)
        add_product_for_test()
        id_product = Product.query.filter_by(name="product_test_1").first().id
        response = client.get(f'/api/product/{id_product+1}', headers={
            "Authorization": token
        })
        delete_product_of_test()
        delete_user_of_test()
        assert response.status_code == 400
        assert json.loads(response.get_data())['data'] == ""
        assert response.is_json


def test_update_product(client):
    with app.app_context():
        new_user = add_user_for_test()
        token = login_user_for_test(new_user, client)
        add_product_for_test()
        id_product = Product.query.filter_by(name="product_test_1").first().id
        json_data = {
            'name': 'product_test_1',
            'description': 'changed description',
            'price': 123.33
        }
        response = client.put(f'/api/product/{id_product}', json=json_data, headers={
            "Content-Type": "application/json", "Authorization": token
        })
        delete_product_of_test()
        delete_user_of_test()
        assert response.status_code == 200
        assert response.is_json
        assert json.loads(response.get_data())['data']
        assert json.loads(response.get_data())['message'], "product modified"


def test_update_product_without_token(client):
    with app.app_context():
        add_product_for_test()
        id_product = Product.query.filter_by(name="product_test_1").first().id
        json_data = {
            'name': 'product_test_1',
            'description': 'changed description',
            'price': 123.33
        }
        response = client.put(f'/api/product/{id_product}', json=json_data, headers={"Content-Type": "application/json"})
        delete_product_of_test()
        assert response.status_code == 400
        assert response.is_json


def test_delete_product(client):
    with app.app_context():
        new_user = add_user_for_test()
        token = login_user_for_test(new_user, client)
        add_product_for_test()
        id_product = Product.query.filter_by(name="product_test_1").first().id
        response = client.delete(f'/api/product/{id_product}', headers={
            "Authorization": token
        })
        delete_product_of_test()
        delete_user_of_test()
        assert response.status_code == 204
        assert response.is_json


def test_delete_product_without_token(client):
    with app.app_context():
        add_product_for_test()
        id_product = Product.query.filter_by(name="product_test_1").first().id
        response = client.delete(f'/api/product/{id_product}')
        delete_product_of_test()
        assert response.status_code == 400
        assert response.is_json