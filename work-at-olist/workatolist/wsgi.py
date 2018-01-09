"""
WSGI config for workatolist project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""
from whitenoise import WhiteNoise

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "workatolist.settings")

application = get_wsgi_application()
application = WhiteNoise(application)