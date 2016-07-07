import os
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ['DJANGO_SETTINGS_MODULE'] = 'mango_core.settings'
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
