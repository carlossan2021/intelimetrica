import os
from run import create_app
import psycopg2 


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'postgresql://olutmpmgofbjru:7de0c54cff76f1347eaebe8e803e0576e167df831b79e3e2cdc5aa54aa219cd5@ec2-54-235-108-217.compute-1.amazonaws.com:5432/d1trrvr1b2n35q'
