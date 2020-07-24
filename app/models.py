from app import app, db
from flask_sqlalchemy import SQLAlchemy



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    fist_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))


    def __init__(self, email, password, fist_name, last_name):
        self.email = email
        self.password = password
        self.fist_name = fist_name
        self.last_name = last_name


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price