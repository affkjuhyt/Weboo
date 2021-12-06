from captcha.helpers import captcha_image_url, captcha_audio_url
from captcha.models import CaptchaStore
from captcha.conf import settings as ca_settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.views import APIView

from authen.urls import auth_urlpatterns
from posts.urls import post_public_urlpatterns, post_urlpatterns
from books.urls import books_public_urlpatterns, books_urlpatterns
from root.settings import base
from userprofile.urls import userprofile_urlpatterns, follow_urlpatterns
from bookcase.urls import history_urlpatterns
from groups.urls import group_public_urlpatterns
from authen import views
from payments import views as payments
from utils.op_drf.response import SuccessResponse

schema_view = get_schema_view(
    openapi.Info(
        title="SAMPLE API",
        default_version='v1',
        description="SAMPLE API DOCS",
    ),
    public=True,
)


class CaptchaRefresh(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        new_key = CaptchaStore.pick()
        to_json_response = {
            "key": new_key,
            "image_url": captcha_image_url(new_key),
            "audio_url": captcha_audio_url(new_key) if ca_settings.CAPTCHA_FLITE_PATH else None,
        }
        return SuccessResponse(to_json_response)


external_public_urlpatterns = books_public_urlpatterns + userprofile_urlpatterns + post_public_urlpatterns \
                              + group_public_urlpatterns
external_urlpatterns = follow_urlpatterns + auth_urlpatterns + history_urlpatterns + books_urlpatterns \
                       + post_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('v1/public/', include(external_public_urlpatterns)),
    path('v1/', include(external_urlpatterns)),
    path('signingg', views.GoogleView.as_view(), name='sigin-gg'),
    path('signinfb', views.FacebookView.as_view(), name='sigin-fb'),
    path('signinapple', views.AppleView.as_view(), name='sigin-apple'),
    path('login', views.LoginAPI.as_view(), name='login'),
    # path('login_admin/', views.LoginAdminAPI.as_view(), name='admin-login'),
    url(r"captcha/refresh/$", CaptchaRefresh.as_view(), name="captcha-refresh"),
    re_path('captcha/', include('captcha.urls')),
    url(r'^test-payment/$', payments.test_payment),
    # re_path('api-token-auth', views.LoginAdminAPI.as_view(), name='api_token_auth'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('logout/', views.LogoutView.as_view()),
    # re_path(r'^getInfo/$', GetUserProfileView.as_view()),
]

if base.DEBUG is True:
    urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
