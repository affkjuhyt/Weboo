import logging

from rest_framework import serializers

from books.models import Book, TagBook, Tag, Chapter
from userprofile.models import DownLoadBook

logger = logging.getLogger(__name__)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'is_enable', 'thumbnail', 'description', 'author', 'date_modified',
                  'date_added', 'sex', 'status', 'type', 'like_count', 'star', 'is_vip']
        read_only_fields = ['id', 'is_enable']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        chapter = Chapter.objects.filter(book=instance.id)
        tag_books = TagBook.objects.filter(book=instance.id)
        user = self.context.get('request').user
        download = DownLoadBook.objects.filter(chapter__in=chapter).filter(user=user)
        count_chapter_download = download.count()
        result = ""
        if tag_books.exists():
            for tag_book in tag_books:
                tag = Tag.objects.filter(id=tag_book.tag.id).first()
                result = result + str(tag.name) + ", "
            result_tag = result[:-2]
            response['tag'] = result_tag
        else:
            response['tag'] = ""

        if chapter.exists():
            response['count_chapter'] = chapter.count()
        else:
            response['count_chapter'] = 0
        breakpoint()
        response['count__chapter_download'] = count_chapter_download

        return response

