import logging

from rest_framework import serializers

from groups.models import Group

logger = logging.getLogger(__name__)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'post_count', 'member_count', 'date_added', 'date_modified', 'is_deleted']
        read_only_fields = ['id']

    def __str__(self):
        return "%s" % self.name
