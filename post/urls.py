from rest_framework_extensions.routers import ExtendedSimpleRouter

from post.apis.v1 import PostView, PostAdminView

public_router = ExtendedSimpleRouter()

public_router.register(
    r'post',
    PostView,
    basename='v1-post'
)

post_public_urlpatterns = public_router.urls

private_router = ExtendedSimpleRouter()

private_router.register(
    r'post',
    PostAdminView,
    basename='v1-post'
)

post_urlpatterns = private_router.urls
