import logging
import math

from django.core.files.storage import Storage
from rest_framework import serializers

from books.models import Chapter, Image
from books.serializers import ImageSerializer
from userprofile.models import DownLoadBook

logger = logging.getLogger(__name__)


class ChapterSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()

    class Meta:
        model = Chapter
        fields = ['id', 'book', 'number', 'title', 'thumbnail', 'date_modified',
                  'date_added', 'like_count', 'is_deleted', 'images', 'size']
        read_only_fields = ['id']

    def get_images(self, obj):
        image = Image.objects.filter(chapter=obj.id)
        return ImageSerializer(image, many=True).data

    def get_size(self, obj):
        images = Image.objects.filter(chapter=obj.id)
        size_bytes = 0
        for image in images:
            size_bytes += image.image.size
        mb_size = size_bytes / 1048574
        return mb_size

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
