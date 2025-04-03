from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g_bgnha**iur$odav61d*(tge+7fj1qn1np)^o0hxetpdh2b3&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

EMAIL_HOST_USER = 'gusserpa02@gmail.com'
EMAIL_HOST_PASSWORD = 'fsfmwbefuvrpvtns'
DEFAULT_FROM_EMAIL = 'gusserpa02@gmail.com'
