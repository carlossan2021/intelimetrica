from flask import request
from flask_restful import Resource
from Model import db, Restaurant, RestaurantSchema
from .utils import is_coordinate_inside_area, get_avg_std

restaurants_schema = RestaurantSchema(many=True)
restaurant_schema = RestaurantSchema()


class StatisticsResource(Resource):

    def get(self,latitude=None,longitude=None,radious=None):
        '''end point que recibe latitud, longitud y radio, 
        para determinar los restaurantes cercanos a esa area
        devuleve un numero'''
        latitude = request.args.get('latitude')
        longitude = request.args.get('longitude')
        radious = request.args.get('radious')

        if latitude == None:
            return {'message': 'Falta la latitude'}, 400
        if longitude == None:
            return {'message': 'Falta la longitud'}, 400
        if radious == None:
            return {'message': 'Falta la radiues'}, 400

        restaurants = Restaurant.query.all()
        restaurants= restaurants_schema.dump(restaurants).data
        restaurants = filter(lambda x: is_coordinate_inside_area(float(latitude), float(longitude), x['lat'], x['lng'], float(radious)), restaurants)
        restaurants = list(restaurants)
        count = len(restaurants)
        avg, std = get_avg_std(restaurants)
        return {'count': count, 'avg': avg, 'std': std}



