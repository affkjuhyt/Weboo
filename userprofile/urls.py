from rest_framework_extensions.routers import ExtendedSimpleRouter

from userprofile.apis.v1 import UserPublicView, UpdateInfo

public_router = ExtendedSimpleRouter()

public_router.register(
    r'user-profile',
    UserPublicView,
    basename='v1-user-profile'
)

public_router.register(
    r'update-account',
    UpdateInfo,
    basename='v1-update-account'
)

userprofile_urlpatterns = public_router.urls
