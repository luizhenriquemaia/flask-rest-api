# in production we would leave in listing out of this file and it would fall back to the values defined in root config.py
from app import app
import os

SECRET_KEY = 'verystrongsecretkey'
basedir = os.path.abspath(os.path.dirname("app"))

# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
