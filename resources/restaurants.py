from flask import request
import json
from flask_restful import Resource
from Model import db, Restaurant, RestaurantSchema
import asyncio

restaurants_schema = RestaurantSchema(many=True)
restaurant_schema = RestaurantSchema()


class RestaurantResource(Resource):
    
    def get(self,id=None):
        '''request para obtener restaurantes por id o general'''
        id = request.args.get('id')
        if id:
            restaurant = Restaurant.query.get(id)
            restaurant = restaurant_schema.dump(restaurant).data
            return {'status': 'success', 'data': restaurant}, 200
        else:
            restaurants = Restaurant.query.all()
            restaurants = restaurants_schema.dump(restaurants).data
            return {'status': 'success', 'data': restaurants}, 200

    def post(self):
        '''request post para la creacion de un nuevo restaurante, se necesitan todos los argumentos'''
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = restaurant_schema.load(json_data)
        if errors:
            return errors, 422
        restaurant = Restaurant.query.filter_by(id=data['id']).first()
        if restaurant:
            return {'message': 'producto already exists'}, 400
        restaurant = Restaurant(_id=data['id'],
                rating=data['rating'],
                name=data['name'],
                site=data['site'],
                email=data['email'],
                phone=data['phone'],
                street=data['street'],
                city=data['city'],
                state=data['state'],
                lat=data['lat'],
                lng=data['lng']
            )
        db.session.add(restaurant)
        db.session.commit()
        result = restaurant_schema.dump(restaurant).data
        return { "status": 'success', 'data': result }, 201

    def put(self):
        ''' request put para la edicion de un restaurante, pueden varias los parametros'''
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = restaurant_schema.load(json_data)
        if errors:
            return errors, 422
        restaurant = Restaurant.query.filter_by(id=data['id']).first()
        if not restaurant:
            return {'message': 'producto does not exist'}, 400
        if 'rating' in data:
            restaurant.rating = data['rating']
        if 'name' in data:
            restaurant.name = data['name']
        if 'site' in data:
            restaurant.site = data['site']
        if 'email' in data:
            restaurant.email = data['email']
        if 'phone' in data:
            restaurant.phone = data['phone']
        if 'street' in data:
            restaurant.street = data['street']
        if 'city' in data:
            restaurant.city = data['city']
        if 'state' in data:
            restaurant.state = data['state']
        if 'lat' in data:
            restaurant.lat = data['lat']
        if 'lng' in data:
            restaurant.lng = data['lng']
            
        db.session.add(restaurant)
        db.session.commit()
        result = restaurant_schema.dump(restaurant).data
        return { "status": 'success', 'data': result}, 201

    def delete(self):
        '''request para eliminar todos los retaurante o por id'''
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = restaurant_schema.load(json_data)
        if errors:
            return errors, 422
        if data['id'] != "todos":
            restaurant = Restaurant.query.filter_by(id=data['id']).first()
            if not restaurant:
                return {'message': 'restaurant does not exist'}, 400
            restaurant = restaurant.query.filter_by(id=data['id']).delete()
            db.session.commit()
            result = restaurant_schema.dump(restaurant).data
            return { "status": 'success', 'data': result}, 201
        else:
            restaurants = Restaurant.query.delete()
            db.session.commit()
            return {'status': 'success', 'data': restaurants}, 200



    