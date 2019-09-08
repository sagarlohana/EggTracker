# models.py
from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # Primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))s
    url = db.Column(db.String(1000))
    price = db.Column(db.String(1000))

class UrlList(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Primary keys are required by SQLAlchemy
    url = db.Column(db.String(1000))

    def __repr__(self):
        return '<Url: {0}>'.format(self.url)