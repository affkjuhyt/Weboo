from rest_framework_extensions.routers import ExtendedSimpleRouter

from books.apis.v1 import BookView, CommentView, CommentPostView, ChapterAdminView, ChapterView, BookAdminView, \
    BookPageView

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

books_public_urlpatterns = public_router.urls

admin_router = ExtendedSimpleRouter()

admin_router.register(
    r'book',
    BookAdminView,
    basename='v1-book'
)

admin_router.register(
    r'comments',
    CommentPostView,
    basename='v1-add-reply'
)

admin_router.register(
    r'chapter',
    ChapterAdminView,
    basename='v1-chapter'
)

admin_router.register(
    r'page',
    BookPageView,
    basename='v1-page'
)

books_urlpatterns = admin_router.urls
