# models.py

from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # Primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    products_available = db.Column(db.Integer)
    total_products = db.Column(db.Integer)
    
class UrlList(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Primary keys are required by SQLAlchemy
    user_id = db.Column(db.Integer)
    url = db.Column(db.String(1000))
    price = db.Column(db.Numeric(10,2))
    def __repr__(self):
        return '<Url: {0}, Price: {1}>'.format(self.url, self.price)