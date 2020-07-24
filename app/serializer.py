from app import app, ma
from .models import User, Product


class UserSerializer(ma.Schema):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'fist_name', 'last_name')


class ProductSerializer(ma.Schema):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price')