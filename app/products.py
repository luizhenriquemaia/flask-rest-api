from app import app, db
from flask import Blueprint, request, jsonify, Response
from .models import Product
from .serializer import ProductSerializer
import json


bp_products = Blueprint('products', __name__)


@bp_products.route('/api/show-products', methods=['GET'])
def list_products():
    serializer = ProductSerializer(many=True)
    query = Product.query.all()
    result = serializer.dump(query)
    if query != []:
        return jsonify(result), 200
    else:
        return jsonify(result), 204


@bp_products.route('/api/product', methods=['POST'])
def add_product():
    serializer = ProductSerializer(many=False)

    if request.method == 'POST':
        if request.is_json:
            name = request.json['name']
            description = request.json['description']
            price = request.json['price']
            new_product = Product(
                name, description, price
            )
            #db.session.add(new_product)
            #db.session.commit()
            response_json = jsonify(
                data=serializer.dump(new_product),
                message="created"
            )
            return response_json, 201
        else:
            return "the request data must be json type", 404

@bp_products.route('/api/product/<id>', methods=['GET', 'DELETE', 'PUT'])
def manage_product(id):
    serializer = ProductSerializer(many=False)
    if request.method == 'GET':
        product = Product.query.get(id)
        response_json = jsonify(
            data=serializer.dump(product),
            message=""
        )
        return response_json, 200



    