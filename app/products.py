from app import app, db
from flask import Blueprint, request, jsonify, Response
from .models import Product
from .serializer import ProductSerializer
import json
from app.authenticate import jwt_required


bp_products = Blueprint('products', __name__)


@bp_products.route('/api/show-products', methods=['GET'])
@jwt_required
def list_products(current_user):
    serializer = ProductSerializer(many=True)
    query = Product.query.all()
    result = serializer.dump(query)
    if query != []:
        return jsonify(result), 200
    else:
        return jsonify(result), 204


@bp_products.route('/api/product', methods=['POST'])
@jwt_required
def add_product(current_user):
    serializer = ProductSerializer(many=False)
    if request.method == 'POST':
        if request.is_json:
            name = request.json['name']
            description = request.json['description']
            price = request.json['price']
            new_product = Product(
                name, description, price
            )
            db.session.add(new_product)
            db.session.commit()
            response_json = jsonify(
                data=serializer.dump(new_product),
                message="created"
            )
            return response_json, 201
        else:
            return jsonify(
                data="",
                message="the request data must be json type"
            ) , 404


@bp_products.route('/api/product/<id>', methods=['GET', 'DELETE', 'PUT'])
@jwt_required
def manage_product(id, current_user):
    serializer = ProductSerializer(many=False)
    if request.method == 'GET':
        product = Product.query.get(id)
        response_json = jsonify(
            data=serializer.dump(product),
            message=""
        )
        return response_json, 200
    
    elif request.method == 'PUT':
        if request.is_json:
            product = Product.query.get(id)
            name = request.json['name']
            description = request.json['description']
            price = request.json['price']
            product.name = name
            product.description = description
            product.price = price
            db.session.commit()
            response_json = jsonify(
                data=serializer.dump(product),
                message="product modified"
            )
            return response_json, 200
        else:
            return jsonify(
                data="",
                message="the request data must be json type"
            ) , 404
    
    elif request.method == 'DELETE':
        product = Product.query.get(id)
        db.session.delete(product)
        db.session.commit()
        response_json = jsonify(
            data="",
            message="product deleted"
        )
        return response_json, 204







    