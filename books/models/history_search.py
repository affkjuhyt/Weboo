import logging

from django.conf import settings
from django.db import models

from utils.base_models import BaseTimeStampModel

logger = logging.getLogger(__name__.split('.')[0])


class HistorySearch(BaseTimeStampModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s"
    )
    text = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return "%s" % self.id
