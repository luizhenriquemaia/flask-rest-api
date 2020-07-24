from flask import Blueprint
from .models import Product
from .serializer import ProductSerializer


bp_products = Blueprint('products', __name__)


@bp_products.route('/show-products', methods=['GET'])
def get():
    serializer = ProductSerializer(many=True)
    query = Product.query.all()
    if query != []:
        return serializer.jsonify(query), 200
    else:
        return serializer.jsonify(query), 204


@bp_products.route('/product', methods=['GET', 'POST', 'DELETE', 'PUT'])
def delete():
    ...