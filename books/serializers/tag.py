import logging

from rest_framework import serializers

from books.models import Tag, TagBook

logger = logging.getLogger(__name__)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'date_modified', 'date_added', 'is_deleted']
        read_only_fields = ['id']


class TagBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagBook
        fields = ['id', 'tag', 'book', 'date_modified', 'date_added', 'is_deleted']
        read_only_fields = ['id']

