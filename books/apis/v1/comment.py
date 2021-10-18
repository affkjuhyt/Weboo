import logging

from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSetMixin

from books.models import Comment, Reply
from books.serializers import CommentSerializer, ReplySerializer

logger = logging.getLogger(__name__.split('.')[0])


class CommentView(ReadOnlyModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    # filter_backends = []
    search_fields = ['content']

    def get_queryset(self):
        return Comment.objects.filter().order_by('-like_count')[:3]


class CommentPostView(ViewSetMixin, generics.RetrieveUpdateAPIView, generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = CommentSerializer(data=request.DATA, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(data=request.DATA)

    def get_queryset(self):
        return Comment.objects.filter()

    @action(detail=True, methods=['post'], url_path='add_reply', serializer_class=CommentSerializer)
    def post_add_reply(self, request, *args, **kwargs):
        comment = self.get_object()
        Reply.objects.create(comment=comment, user=request.user.id)

        return Response('Create reply is successfully.', status=status.HTTP_200_OK)
