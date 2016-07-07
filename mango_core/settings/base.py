import json
import os
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROPERTIES_FILE = os.path.join(BASE_DIR, os.environ.get('properties_file', 'properties.json'))
if not os.path.exists(PROPERTIES_FILE):
    PROPERTIES_FILE = os.path.join(BASE_DIR, 'properties.json')

try:
    host_properties = json.load(open(PROPERTIES_FILE))
except IOError:
    raise ImproperlyConfigured("Cannot read properties file at %s" % PROPERTIES_FILE)

SECRET_KEY = host_properties['host']['django_secret_key']

DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'request_id',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'mango_core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': host_properties['database']
}

LANGUAGE_CODE = 'en'

ugettext = lambda s: s

LANGUAGES = (
    ('en', ugettext('English')),
    # ('fr', ugettext('French')),
)

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'), )

SITE_ID = 1

TIME_ZONE = 'Europe/Brussels'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = ''
MEDIA_URL = ''


LOG_FILENAME = host_properties['host']['log_file']
if len(LOG_FILENAME) > 0 and LOG_FILENAME[0] != '/':
    # If not absolute path, put them in logs/xxx.log
    LOG_FILENAME = os.path.join(BASE_DIR, '..', 'logs', LOG_FILENAME)
elif len(LOG_FILENAME) == 0:
    LOG_FILENAME = 'django.log'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        "request_id": {
            "()": "request_id.logging.RequestIdFilter"
        }
    },
    'formatters': {
        'verbose': {
            'format': "[%(request_id)s] [%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOG_FILENAME,
            'formatter': 'verbose',
            'filters': ['request_id'],
        },
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {},
        },
    },
    'loggers': {
        'nrpy': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': [],
        },
        '': {
            'handlers': ['logfile', 'sentry'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

if 'raven_dsn' in host_properties['host'] and host_properties['host']['raven_dsn']:
    RAVEN_CONFIG = {
        'dsn': host_properties['host']['raven_dsn']
    }
    # Uncomment the following to add release information to sentry reports
    #try:
    #    with open('APP_NAME/__init__.py', 'r') as fd:
    #        RAVEN_CONFIG['release'] = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)
    #except IOError:
    #    RAVEN_CONFIG['release'] = 'unknown'
    INSTALLED_APPS += (
        'raven.contrib.django',
    )