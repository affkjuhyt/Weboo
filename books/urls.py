from rest_framework_extensions.routers import ExtendedSimpleRouter

from books.apis.v1 import BookView, CommentView, CommentPostView, ChapterView, BookAdminView

public_router = ExtendedSimpleRouter()

public_router.register(
    r'books',
    BookView,
    basename='v1-books'
)

public_router.register(
    r'chapters',
    ChapterView,
    basename='v1-chapters'
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

admin_router = ExtendedSimpleRouter()

admin_router.register(
    r'book',
    BookAdminView,
    basename='v1-book'
)

books_urlpatterns = admin_router.urls
