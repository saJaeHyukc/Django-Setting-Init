from config.settings.base import *

if SERVER_ENV == "dev":
    ALLOWED_HOSTS = ["*"]

    DEBUG = True

    # Database settings
    IS_DEV_DB = ast.literal_eval(env("IS_DEV_DATABASE"))

    if IS_DEV_DB:
        pymysql.install_as_MySQLdb()
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.mysql",
                "NAME": env("DEV_DB_NAME"),
                "USER": env("DEV_DB_USER"),
                "PASSWORD": env("DEV_DB_PASSWORD"),
                "HOST": env("DEV_DB_HOST"),
                "PORT": env("DEV_DB_PORT"),
            },
        }

    # CORS/CSRF settings
    CORS_ALLOW_CREDENTIALS = True
    CORS_ORIGIN_WHITELIST = []
    CSRF_TRUSTED_ORIGINS = CORS_ORIGIN_WHITELIST
