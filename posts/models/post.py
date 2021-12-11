import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

from groups.models import Group
from utils.base_models import BaseTimeStampModel

logger = logging.getLogger(__name__.split('.')[0])

User = get_user_model()


class Post(BaseTimeStampModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="%(class)s"
    )
    group = models.ForeignKey(Group, null=True, on_delete=models.CASCADE)
    content = models.TextField(max_length=2000, null=True, blank=True)
    like_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
