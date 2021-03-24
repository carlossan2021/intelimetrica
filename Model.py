from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

ma = Marshmallow()
db = SQLAlchemy()


class Restaurant(db.Model,SerializerMixin):
    __tablename__ = 'restaurant'
    id = db.Column(db.String(100), primary_key=True)
    rating = db.Column(db.Integer)
    name = db.Column(db.String(100))
    site = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    street = db.Column(db.String(100))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    serialize_only=('rating', 'name', 'site', 'email', 'phone', 'street', 'city', 'state', 'lat', 'lgn')

    def __init__(self, _id,rating, name, site, email, phone, street, city, state, lat, lng):
        self.id = _id
        self.rating = rating
        self.name = name
        self.site = site
        self.email = email
        self.phone = phone
        self.street = street
        self.city = city
        self.state = state
        self.lat = lat
        self.lng =lng

class RestaurantSchema(ma.Schema):
    id = fields.String()
    rating = fields.Integer()
    name = fields.String()
    site = fields.String()
    email = fields.String()
    phone = fields.String()
    street = fields.String()
    city = fields.String()
    state = fields.String()
    lat = fields.Float()
    lng = fields.Float()


