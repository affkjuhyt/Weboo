import logging

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from books.models import Tag
from books.serializers import TagSerializer

logger = logging.getLogger(__name__.split('.')[0])


class TagView(ReadOnlyModelViewSet):
    serializer_class = TagSerializer
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return Tag.objects.filter().order_by('?')

