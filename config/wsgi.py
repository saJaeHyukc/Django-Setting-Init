import os

from django.core.wsgi import get_wsgi_application

from config.settings.base import SERVER_ENV

if SERVER_ENV == "local":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

elif SERVER_ENV == "dev":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")

elif SERVER_ENV == "prod":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.prod")

application = get_wsgi_application()
