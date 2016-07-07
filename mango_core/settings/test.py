import os

os.environ['properties_file'] = 'properties.test.json'
from .base import *

ENV = 'TEST'

DEBUG = False

ALLOWED_HOSTS = ['.eurid.eu', ]
