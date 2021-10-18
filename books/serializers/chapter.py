import logging

from rest_framework import serializers

from books.models import Chapter

logger = logging.getLogger(__name__)


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'book', 'title', 'thumbnail', 'date_modified',
                  'date_added', 'like_count', 'is_deleted']
        read_only_fields = ['id']
