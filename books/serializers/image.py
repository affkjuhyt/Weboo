import logging

from rest_framework import serializers

from books.models import Image

logger = logging.getLogger(__name__)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'chapter', 'image', 'date_modified', 'date_added', 'is_deleted']
        read_only_fields = ['id']

