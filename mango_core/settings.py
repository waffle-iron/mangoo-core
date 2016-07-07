import json
import os
from django.core.exceptions import ImproperlyConfigured
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = "jyghqie2a+r_m9wp02w%9h6#*y+5$)12ac!a6jxv^7j43e#kth&g6+54-"

DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'request_id',
)

MIDDLEWARE_CLASSES = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
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
        'DIRS': [os.path.join(BASE_DIR, '../mango_core/templates')]
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
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
    }
}

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


ugettext = lambda s: s

LANGUAGES = (
    ('en', ugettext('English')),
    # ('fr', ugettext('French')),
)

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)

SITE_ID = 1
TIME_ZONE = 'Europe/Brussels'
LANGUAGE_CODE = 'en'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = ''
MEDIA_URL = ''

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

LOG_FILENAME = "mango_core.log"
if len(LOG_FILENAME) > 0 and LOG_FILENAME[0] != '/':
    # If not absolute path, put them in logs/xxx.log
    LOG_FILENAME = os.path.join(BASE_DIR, 'logs', LOG_FILENAME)
elif len(LOG_FILENAME) == 0:
    LOG_FILENAME = 'django.log'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'testlogger': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         },
#         "request_id": {
#             "()": "request_id.logging.RequestIdFilter"
#         }
#     },
#     'formatters': {
#         'verbose': {
#             'format': "[%(request_id)s] [%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#             'datefmt': "%d/%b/%Y %H:%M:%S"
#         },
#     },
#     'handlers': {
#         'logfile': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': LOG_FILENAME,
#             'formatter': 'verbose',
#             'filters': ['request_id'],
#         },
#         'sentry': {
#             'level': 'WARNING',
#             'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
#             'tags': {},
#         },
#     },
#     'loggers': {
#         'nrpy': {
#             'handlers': ['logfile'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['logfile'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'django.db.backends': {
#             'handlers': [],
#         },
#         '': {
#             'handlers': ['logfile', 'sentry'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     }
# }

# if 'raven_dsn' in host_properties['host'] and host_properties['host']['raven_dsn']:
#     RAVEN_CONFIG = {
#         'dsn': host_properties['host']['raven_dsn']
#     }
    # Uncomment the following to add release information to sentry reports
    # try:
    #    with open('APP_NAME/__init__.py', 'r') as fd:
    #        RAVEN_CONFIG['release'] = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)
    # except IOError:
    #    RAVEN_CONFIG['release'] = 'unknown'
    # INSTALLED_APPS += (
    #     'raven.contrib.django',
    # )

# try to load local_settings.py if it exists
try:
    from local_settings import *
except Exception as e:
    pass
