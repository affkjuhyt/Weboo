import logging

from rest_framework import serializers

from post.models import Post

logger = logging.getLogger(__name__)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'group', 'content', 'like_count', 'share_count',
                  'date_added', 'date_modified', 'is_deleted']
