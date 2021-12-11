import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from books.models import Book, Chapter

from utils.base_models import BaseTimeStampModel

User = get_user_model()

logger = logging.getLogger(__name__.split('.')[0])


class Comment(BaseTimeStampModel):
    book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s")
    content = models.TextField(null=True, blank=True)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return "%s" % self.id


class Reply(BaseTimeStampModel):
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    reply = models.TextField(null=True, blank=True)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return "%s" % self.user.full_name

    @property
    def get_replies(self):
        return self.replies.all()
