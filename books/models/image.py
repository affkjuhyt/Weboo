import logging

from django.db import models
from .chapter import Chapter

from utils.base_models import BaseTimeStampModel

logger = logging.getLogger(__name__.split('.')[0])


class Image(BaseTimeStampModel):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    image = models.FileField(
        upload_to='books/%Y/%m/%d',
        null=True
    )

    def __str__(self):
        return "%s" % self.id
