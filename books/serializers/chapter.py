import logging

from rest_framework import serializers

from books.models import Chapter
from userprofile.models import DownLoadBook

logger = logging.getLogger(__name__)


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'book', 'number', 'title', 'thumbnail', 'date_modified',
                  'date_added', 'like_count', 'is_deleted']
        read_only_fields = ['id']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        user = self.context.get('request').user
        chapter_ids = DownLoadBook.objects.filter(user=user).filter(chapter=instance).exclude(
            status=[DownLoadBook.NOT_DOWNLOAD]).values_list('chapter_id',
                                                                                flat=True)
        if instance.id in chapter_ids:
            chapter_downloaded = DownLoadBook.objects.filter(user=user).filter(chapter=instance).exclude(
                status=[DownLoadBook.NOT_DOWNLOAD, DownLoadBook.ERROR]).first()
            response['status_download'] = chapter_downloaded.status
        else:
            response['status_download'] = DownLoadBook.NOT_DOWNLOAD

        return response
