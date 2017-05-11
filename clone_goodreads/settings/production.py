from .base import *
import dj_database_url
import os

SECRET_KEY = 'uo*a=9+3enc3zu(i8hx&%p=&&qyzxikncag!rvmr^@rbs62xk^'

DATABASES = dict()
DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO','https')

ALLOWED_HOSTS = ['*']

DEBUG = False

STATIC_ROOT = os.path.join(os.getcwd(),'static')