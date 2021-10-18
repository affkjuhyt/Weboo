from django.conf.urls import url
from django.urls import include
from rest_framework.routers import SimpleRouter

from authen.apis.v1 import RegisterViewSet, LoginAPI, PasswordViewSet

router = SimpleRouter()
router.register(
    r'register',
    RegisterViewSet,
    basename='register'
)

router.register(
    r'login',
    LoginAPI,
    basename='login'
)

router.register(
    r'passwords',
    PasswordViewSet,
    basename='passwords'
)

auth_urlpatterns = [
    url(r'^auth/', include(router.urls)),
]
