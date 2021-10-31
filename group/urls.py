from rest_framework_extensions.routers import ExtendedSimpleRouter

from group.apis.v1 import GroupView

public_router = ExtendedSimpleRouter()

public_router.register(
    r'group',
    GroupView,
    basename='v1-group'
)

group_public_urlpatterns = public_router.urls
