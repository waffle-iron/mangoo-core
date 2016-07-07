import os

os.environ['properties_file'] = 'properties.json'
from .base import *

ENV = 'DEVELOPMENT'

DEBUG = True

ALLOWED_HOSTS = ['api.mangoapp.io', ]
