"""
WSGI config for personal_center project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Auto-select settings: use prod if DATABASE_URL is present (Vercel), else dev
if os.environ.get("DATABASE_URL"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personal_center.settings.prod")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personal_center.settings.dev")

application = get_wsgi_application()
