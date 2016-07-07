import os

os.environ['properties_file'] = 'properties.staging.json'
from .base import *

ENV = 'STAGING'

DEBUG = False

ALLOWED_HOSTS = ['api.mangoapp.io', ]
