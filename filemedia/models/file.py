import logging

from django.db import models

from post.models import Post
from utils.base_models import BaseTimeStampModel

logger = logging.getLogger(__name__.split('.')[0])


class File(BaseTimeStampModel):
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    file = models.FileField(
        upload_to='books/%Y/%m/%d',
        null=True
    )

    def __str__(self):
        return "%s" % self.id
