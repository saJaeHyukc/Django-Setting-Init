import os

from django.core.asgi import get_asgi_application

from config.settings.base import SERVER_ENV

if SERVER_ENV == "local":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

elif SERVER_ENV == "dev":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")

elif SERVER_ENV == "prod":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.prod")

application = get_asgi_application()
