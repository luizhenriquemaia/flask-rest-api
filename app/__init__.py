from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


# init app
app = Flask(__name__, instance_relative_config=True)
# load the default configuration
app.config.from_object('config.default')
# load configurations variables from an instance folder
app.config.from_pyfile('config.py')
# load configurations variables for development enviroment
app.config.from_object('config.development')

# init db
db = SQLAlchemy(app)

# init ma
ma = Marshmallow(app)


# blueprints
from .products import bp_products
app.register_blueprint(bp_products)
