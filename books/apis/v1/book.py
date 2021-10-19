import logging

from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSetMixin
from rest_framework.filters import SearchFilter

from books.models import Book, Comment
from books.serializers import BookSerializer, CommentSerializer

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
