import logging

from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from root.authentications import BaseUserJWTAuthentication
from books.models import Book, Chapter
from userprofile.models import DownLoadBook
from books.serializers import BookSerializer, ChapterSerializer
from bookcase.models import History
from rest_framework.viewsets import ViewSetMixin

logger = logging.getLogger(__name__.split('.')[0])


class ChapterView(ViewSetMixin, generics.RetrieveUpdateAPIView, generics.ListCreateAPIView):
    serializer_class = ChapterSerializer
    authentication_classes = [BaseUserJWTAuthentication]
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Chapter.objects.filter()

    @action(detail=True, methods=['post'], url_path='action_chapter', serializer_class=ChapterSerializer)
    def post_action_chapter(self, request, *args, **kwargs):
        user = self.request.user
        chapter = self.get_object()
        book = Book.objects.filter(chapter=chapter).first()

        history = History.objects.filter(user=user, book=book).first()
        if history.DoesNotExist:
            if history.chapter_id > chapter.number:
                pass
            else:
                history.chapter = chapter
                history.save()
        else:
            History.objects.create(user=user, book=book, chapter=chapter)

        return Response('Write log success', status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='delete_download')
    def post_delete_download(self, request, *args, **kwargs):
        chapter = self.get_object()
        download_book = DownLoadBook.objects.filter(chapter=chapter).filter(user=self.request.user)
        if len(download_book) > 0:
            download_book.update(status=DownLoadBook.NOT_DOWNLOAD)

            return Response("Delete book downloaded successfully", status=status.HTTP_200_OK)
        else:
            return Response("Khong co chapter nay", status=status.HTTP_404_NOT_FOUND)
