import logging

from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSetMixin

from books.models import Comment
from books.serializers import CommentSerializer
from root.authentications import BaseUserJWTAuthentication

logger = logging.getLogger(__name__.split('.')[0])


class CommentView(ReadOnlyModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    search_fields = ['content']

    def get_queryset(self):
        return Comment.objects.filter().order_by('-like_count')[:3]


class CommentPostView(ViewSetMixin, generics.RetrieveUpdateAPIView, generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [BaseUserJWTAuthentication]
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def post(self, request):
        serializer = CommentSerializer(data=request.DATA, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(data=request.DATA)

    def get_queryset(self):
        return Comment.objects.filter()
