from app import app
from flask_sqlalchemy import SQLAlchemy

# init db
db = SQLAlchemy(app)


#class Product(db.Model):
#    id = db.Column()