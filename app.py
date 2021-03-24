from flask import Blueprint
from flask_restful import Api
from resources.statistics import StatisticsResource
from resources.restaurants import RestaurantResource


api_bp = Blueprint('restaurants', __name__)
api = Api(api_bp)

# Route
api.add_resource(StatisticsResource, '/statistics')
api.add_resource(RestaurantResource, '/')
