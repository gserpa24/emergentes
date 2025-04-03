from datetime import timedelta
from pathlib import Path

import os
from os import environ as env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = env['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []

# Application definition

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'dj_rest_auth',
    'dj_rest_auth.registration',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',

    'drf_yasg',
]

LOCAL_APP = []

THIRD_APPS = [
    'apps.nucleo'
]

INSTALLED_APPS = BASE_APPS + LOCAL_APP + THIRD_APPS

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#    'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': env['DB_NAME'],
#         'USER': env['DB_USER'],
#         'PASSWORD': env['DB_PASSWORD'],
#         'HOST': env['DB_HOST'],
#         'PORT': env['DB_PORT'],
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_UNIQUE_EMAIL = True

AUTHENTICATION_BACKENDS = [
    # Permite el login tradicional con usuario en el admin de Django.
    'django.contrib.auth.backends.ModelBackend',
    # Permite autenticación con emai
    'allauth.account.auth_backends.AuthenticationBackend',
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
# EMAIL_HOST_USER = env['EMAIL_HOST_USER']
# EMAIL_HOST_PASSWORD = env['EMAIL_HOST_PASSWORD']
# DEFAULT_FROM_EMAIL = env['DEFAULT_FROM_EMAIL']

REST_FRAMEWORK = {
    # Usa los permisos estandares de 'django.contrib.auth',
    # o permite el acceso solo lectura para usuarios no autenticados.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_HTTPONLY': False,
    'JWT_AUTH_COOKIE': 'core-app-auth',
    'JWT_AUTH_REFRESH_COOKIE': 'core-refresh-token',
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=90),
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {'type': 'apiKey', 'name': 'Authorization', 'in': 'header'}
    }
}

CSRF_TRUSTED_ORIGINS = ['http://*']

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'home/static'),
]
