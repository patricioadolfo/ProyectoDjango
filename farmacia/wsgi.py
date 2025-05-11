"""
WSGI config for farmacia project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

path = '/var/www/ProyectoDjango'

if path not in sys.path:
    sys.path.append(path)


from django.core.wsgi import get_wsgi_application

os.environ["DJANGO_SETTINGS_MODULE"]= 'farmacia.settings'

application = get_wsgi_application()
