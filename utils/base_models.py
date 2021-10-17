#!/usr/bin/python
# -*- coding: utf-8 -*-
import uuid

from django.conf import settings
from django.db import models


class BaseTimeStampModel(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class BaseUserModel(BaseTimeStampModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s"
    )

    class Meta:
        abstract = True


class BaseForeignKeyUserModel(BaseTimeStampModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True


class BaseModel(BaseTimeStampModel):
    class Meta:
        abstract = True


class BaseUUIDModel(BaseTimeStampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
