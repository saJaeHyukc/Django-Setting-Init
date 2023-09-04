from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

from config.settings.base import SERVER_ENV

urlpatterns = []

# Local Server Debug Toolbar
if SERVER_ENV == "local":
    import debug_toolbar

    urlpatterns += [re_path(r"^__debug__/", include(debug_toolbar.urls))]


# Local or Dev Server Swagger Docs
if SERVER_ENV in ["local", "dev"]:
    schema_view = get_schema_view(
        openapi.Info(
            title="Django Setting",
            default_version="v1",
            description="",
            terms_of_service="",
            contact=openapi.Contact(email=""),
            license=openapi.License(name=""),
        ),
        public=True,
        permission_classes=(AllowAny,),
    )

    urlpatterns += [
        path("swagger/docs", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
        path("swagger/redoc", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    ]

# All Server URLs
urlpatterns += [
    # Admin
    path("admin/", admin.site.urls),
    # API V1
]


# Static/Media File Root (CSS, JavaScript, Images)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
