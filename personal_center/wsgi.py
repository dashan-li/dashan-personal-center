"""
WSGI config for personal_center project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import sys
import logging

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logger = logging.getLogger(__name__)

db_url = os.environ.get("DATABASE_URL", "")
dsm = os.environ.get("DJANGO_SETTINGS_MODULE", "")

logger.info(f"[WSGI INIT] DATABASE_URL present: {bool(db_url)}, prefix: {db_url[:30] if db_url else 'NONE'}")
logger.info(f"[WSGI INIT] DJANGO_SETTINGS_MODULE env: '{dsm}'")

if db_url:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personal_center.settings.prod")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personal_center.settings.dev")

logger.info(f"[WSGI INIT] Final DJANGO_SETTINGS_MODULE: '{os.environ.get('DJANGO_SETTINGS_MODULE')}'")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

logger.info("[WSGI INIT] Django application loaded OK")
