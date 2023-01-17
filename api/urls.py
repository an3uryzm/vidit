from rest_framework import routers
from django.urls import path, include, re_path
from api.views import PhotoViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r"photos", PhotoViewSet, basename="photo")


schema_view = get_schema_view(
    openapi.Info(
        title="Photo Manager API",
        default_version='v1',
        description="API to manage photos",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="an3uryzm@gmail.com"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
]
