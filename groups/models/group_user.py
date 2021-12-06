import logging

from django.conf import settings
from django.db import models

from utils.base_models import BaseTimeStampModel
from groups.models import Group

logger = logging.getLogger(__name__.split('.')[0])


class GroupUser(BaseTimeStampModel):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s"
    )

    def __str__(self):
        return "%s" % self.id
