import logging

from rest_framework import serializers

from filemedia.models import Video

logger = logging.getLogger(__name__)


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'post', 'video', 'date_added', 'date_modified', 'is_deleted']
        read_only_fields = ['id']
