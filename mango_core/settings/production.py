import os

os.environ['properties_file'] = 'properties.production.json'
from .base import *

ENV = 'PRODUCTION'

DEBUG = False

ALLOWED_HOSTS = ['api.mangoapp.io', ]
