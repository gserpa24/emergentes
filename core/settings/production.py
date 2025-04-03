import os
from core.logging import *
from core.settings.base import *
from dotenv import load_dotenv

load_dotenv(Path.joinpath(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*', 'emergentes-production.up.railway.app']

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
    #        'ENGINE': 'django.db.backends.mysql',
    #        'NAME': env['DB_NAME'],
    #        'USER': env['DB_USER'],
    #        'PASSWORD': env['DB_PASSWORD'],
    #        'HOST': env['DB_HOST'],
    #        'PORT': env['DB_PORT'],
}

STATIC_ROOT = Path.joinpath(BASE_DIR, 'staticfiles')

EMAIL_HOST_USER = env['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = env['EMAIL_HOST_PASSWORD']
DEFAULT_FROM_EMAIL = env['DEFAULT_FROM_EMAIL']

CSRF_TRUSTED_ORIGINS = ['http://*', 'https://emergentes-production.up.railway.app']

# CORS_ALLOW_ALL_ORIGINS = True

# Permitir solo dominios específicos:
CORS_ALLOWED_ORIGINS = [
    'https://emergentes-production.up.railway.app',
    'http://localhost:8000',
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']
CORS_ALLOW_HEADERS = ['authorization', 'content-type']

