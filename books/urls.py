from rest_framework_extensions.routers import ExtendedSimpleRouter

from books.apis.v1 import BookView, CommentView, CommentPostView

public_router = ExtendedSimpleRouter()

public_router.register(
    r'books',
    BookView,
    basename='v1-books'
)

public_router.register(
    r'comments',
    CommentView,
    basename='v1-comments'
)

public_router.register(
    r'comments',
    CommentPostView,
    basename='v1-add-reply'
)

books_public_urlpatterns = public_router.urls
