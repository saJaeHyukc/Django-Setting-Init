from config.settings.base import *

if SERVER_ENV == "local":
    ALLOWED_HOSTS = ["*"]

    DEBUG = True

    # Debug Toolbar settings
    if DEBUG:
        MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
        INSTALLED_APPS += ("debug_toolbar",)
        DEBUG_TOOLBAR_PANELS = [
            "debug_toolbar.panels.versions.VersionsPanel",
            "debug_toolbar.panels.timer.TimerPanel",
            "debug_toolbar.panels.settings.SettingsPanel",
            "debug_toolbar.panels.headers.HeadersPanel",
            "debug_toolbar.panels.request.RequestPanel",
            "debug_toolbar.panels.sql.SQLPanel",
            "debug_toolbar.panels.staticfiles.StaticFilesPanel",
            "debug_toolbar.panels.templates.TemplatesPanel",
            "debug_toolbar.panels.cache.CachePanel",
            "debug_toolbar.panels.signals.SignalsPanel",
            "debug_toolbar.panels.logging.LoggingPanel",
            "debug_toolbar.panels.redirects.RedirectsPanel",
        ]
        DEBUG_TOOLBAR_CONFIG = {
            "INTERCEPT_REDIRECTS": False,
        }

    # Database settings
    IS_LOCAL_DB = ast.literal_eval(env("IS_LOCAL_DATABASE"))

    if IS_LOCAL_DB:
        pymysql.install_as_MySQLdb()
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.mysql",
                "NAME": env("LOCAL_DB_NAME"),
                "USER": env("LOCAL_DB_USER"),
                "PASSWORD": env("LOCAL_DB_PASSWORD"),
                "HOST": env("LOCAL_DB_HOST"),
                "PORT": env("LOCAL_DB_PORT"),
            },
        }
    else:
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": BASE_DIR / "db.sqlite3",
            }
        }

    # CORS/CSRF settings
    CORS_ALLOW_CREDENTIALS = True
    CORS_ORIGIN_WHITELIST = []
    CSRF_TRUSTED_ORIGINS = CORS_ORIGIN_WHITELIST
