from .base import *
import os
import dj_database_url

DEBUG = False
# Allow all *.vercel.app subdomains plus any custom hosts from env
ALLOWED_HOSTS = ['*']  # Temporarily open for debugging; restrict after login is confirmed working

MIDDLEWARE += ['personal_center.middleware.LoginDebugMiddleware']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {'handlers': ['console'], 'level': 'DEBUG'},
        'django.request': {'handlers': ['console'], 'level': 'DEBUG'},
        'django.security': {'handlers': ['console'], 'level': 'DEBUG'},
        'django.contrib.auth': {'handlers': ['console'], 'level': 'DEBUG'},
        'django.contrib.sessions': {'handlers': ['console'], 'level': 'DEBUG'},
    },
}

# Database — Neon PostgreSQL via DATABASE_URL env var
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True,
    )
}

# Cloudinary for media uploads
INSTALLED_APPS += ['cloudinary', 'cloudinary_storage']

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = '/media/'

# Vercel terminates TLS at the proxy level; tell Django to trust the forwarded header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False  # Vercel handles HTTPS redirect, not Django

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Required by Django 4+ for CSRF validation on POST requests (e.g. admin login)
CSRF_TRUSTED_ORIGINS = [
    'https://dashan.vercel.app',
    'https://personalcenter.vercel.app',
]
