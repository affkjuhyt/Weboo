import logging

from django.db import models
from django.conf import settings
from books.models import Book, Chapter

from utils.base_models import BaseTimeStampModel

logger = logging.getLogger(__name__.split('.')[0])


class History(BaseTimeStampModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s"
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    hide = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.id
