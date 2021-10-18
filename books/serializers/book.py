import logging

from rest_framework import serializers

from books.models import Book

logger = logging.getLogger(__name__)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'is_enable', 'thumbnail', 'description', 'author', 'date_modified',
                  'date_added', 'sex', 'status', 'type', 'like_count', 'star', 'is_vip']
        read_only_fields = ['id', 'is_enable']

