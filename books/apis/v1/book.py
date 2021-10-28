import logging

from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSetMixin
from rest_framework.filters import SearchFilter

from bookcase.models import History
from books.models import Book, Comment, TagBook, Tag
from books.serializers import BookSerializer, CommentSerializer
from userprofile.models import FollowBook
from root.authentications import BaseUserJWTAuthentication

logger = logging.getLogger(__name__.split('.')[0])


class BookView(ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    filter_backends = [SearchFilter]
    filter_fields = ['is_enable']
    search_fields = ['title']

    def get_queryset(self):
        return Book.objects.filter(is_enable=True).order_by('-date_added')

    @action(detail=True, methods=['get'], url_path='total_comment', serializer_class=CommentSerializer)
    def get_comment(self, request, *args, **kwargs):
        book = self.get_object()

        paginator = PageNumberPagination()
        paginator.page_size = 10

        comments = Comment.objects.filter(book=book).order_by('-like_count')
        result_page = paginator.paginate_queryset(comments, request)
        list_comments = CommentSerializer(result_page, context={"request": request}, many=True)

        return paginator.get_paginated_response(list_comments.data)

    @action(detail=True, methods=['get'], url_path='comment_out_standing', serializer_class=CommentSerializer)
    def get_comment_out_standing(self, *args, **kwargs):
        book = self.get_object()
        comment = Comment.objects.filter(book=book).order_by('-like_count')[:3]
        serializer = CommentSerializer(comment, many=True)

        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='suggest_book')
    def get_suggest_book(self, request, *args, **kwargs):
        paginator = PageNumberPagination()
        paginator.page_size = 10

        book = Book.objects.filter().order_by('-star')
        result_page = paginator.paginate_queryset(book, request)
        list_suggest_books = BookSerializer(result_page, context={"request": request}, many=True)

        return paginator.get_paginated_response(list_suggest_books.data)


class BookAdminView(ViewSetMixin, generics.RetrieveUpdateAPIView, generics.ListCreateAPIView):
    serializer_class = BookSerializer
    authentication_classes = [BaseUserJWTAuthentication]
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Book.objects.filter()

    @action(detail=False, methods=['get'], url_path='relate_to', serializer_class=BookSerializer)
    def get_relate_to(self, request, *args, **kwargs):
        paginator = PageNumberPagination()
        paginator.page_size = 10
        user = self.request.user
        list_history = History.objects.filter(user=user)
        if len(list_history) > 0:
            for history in list_history:
                book = Book.objects.filter(id=history.book.id).first()
                tag_book_ids = TagBook.objects.filter(book_id=book.id).values_list('id', flat=True)
                tag_ids = Tag.objects.filter(tagbook__in=tag_book_ids).values_list('id', flat=True)
                tag_book_list = TagBook.objects.filter(tag__in=tag_ids).values_list('book_id', flat=True)
                books = Book.objects.filter(pk__in=tag_book_list)
                result_page = paginator.paginate_queryset(books, request)
                serializer = BookSerializer(result_page, context={"request": request}, many=True)
                return paginator.get_paginated_response(serializer.data)
        else:
            return Response("Khong co truyen lien quan")

    @action(detail=True, methods=['post'], url_path='follow_book')
    def post_follow_book(self, request, *args, **kwargs):
        try:
            book = self.get_object()
            user = self.request.user
            follow = FollowBook.objects.filter(user=user, book=book).first()
            if follow.DoesNotExist:
                if follow.status:
                    follow.status = False
                else:
                    follow.status = True
                follow.save()
            else:
                FollowBook.objects.create(book=book, user=user)
            return Response("Create follow success", status=status.HTTP_200_OK)
        except:
            return Response("Error", status=status.HTTP_404_NOT_FOUND)
