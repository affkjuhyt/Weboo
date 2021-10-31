import logging

from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin, ReadOnlyModelViewSet

from post.models import Post
from post.serializers import PostSerializer
from root.authentications import BaseUserJWTAuthentication

logger = logging.getLogger(__name__.split('.')[0])


class PostView(ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    filter_backends = [SearchFilter]

    def get_queryset(self):
        return Post.objects.filter()

    @action(detail=False, methods=['get'], url_path='post_trending')
    def get_post_trending(self, request, *args, **kwargs):
        posts = Post.objects.order_by('-like_count', 'share_count')
        paginator = PageNumberPagination()
        paginator.page_size = 10

        result_page = paginator.paginate_queryset(posts, request)
        list_comments = PostSerializer(result_page, context={"request": request}, many=True)

        return paginator.get_paginated_response(list_comments.data)


class PostAdminView(ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    authentication_classes = [BaseUserJWTAuthentication]
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    filter_backends = [SearchFilter]

    def get_queryset(self):
        return Post.objects.filter()

    @action(detail=False, methods=['get'], url_path='post_user')
    def get_post_user(self, request, *args, **kwargs):
        user = self.request.user
        posts = Post.objects.filter(user=user)
        paginator = PageNumberPagination()
        paginator.page_size = 10

        result_page = paginator.paginate_queryset(posts, request)
        list_comments = PostSerializer(result_page, context={"request": request}, many=True)

        return paginator.get_paginated_response(list_comments.data)

