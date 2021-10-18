from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from authen.urls import auth_urlpatterns
from books.urls import books_public_urlpatterns
from userprofile.urls import userprofile_urlpatterns
from authen import views

schema_view = get_schema_view(
    openapi.Info(
        title="SAMPLE API",
        default_version='v1',
        description="SAMPLE API DOCS",
    ),
    public=True,
)

external_public_urlpatterns = books_public_urlpatterns + userprofile_urlpatterns
external_urlpatterns = auth_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('v1/public/', include(external_public_urlpatterns)),
    path('v1/', include(external_urlpatterns)),
    path('signingg', views.GoogleView.as_view(), name='sigin-gg'),
    path('signinfb', views.FacebookView.as_view(), name='sigin-fb'),
    path('signinapple', views.AppleView.as_view(), name='sigin-apple'),
]
