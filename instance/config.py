# in production we would leave in listing out of this file and it would fall back to the values defined in root config.py
from app import app
import os

SECRET_KEY = 'verystrongsecretkey'
basedir = os.path.abspath(os.path.dirname("app"))

# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/system_verzel'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
