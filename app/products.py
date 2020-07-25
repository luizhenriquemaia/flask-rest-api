from . import db
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


@bp_products.route('/api/product', methods=['GET', 'POST', 'DELETE', 'PUT'])
def product_api():
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
            return Response(response={'data': new_product, 'message': "created"}, status=201)
        else:
            return Response(response={'data': '', 'message': "bad request"}, status=404)
    
    #elif request.method == 'GET':

    