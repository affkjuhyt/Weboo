from django.conf import settings
from django.db import models
from django.db.models import *

from apps.vadmin.op_drf.fields import UpdateDateTimeField, CreateDateTimeField
from apps.vadmin.op_drf.models import CoreModel


class MessagePush(CoreModel):
    title = CharField(max_length=128, verbose_name="Notification title")
    content = TextField(verbose_name="Notification content")
    message_type = CharField(max_length=8, verbose_name="Notification type")
    is_reviewed = BooleanField(default=True, verbose_name="Whether to review")
    status = CharField(max_length=8, verbose_name="Notification status")
    to_path = CharField(max_length=256, verbose_name="Jump path", null=True, blank=True, )
    user = ManyToManyField(to=settings.AUTH_USER_MODEL,
                           related_name="user", related_query_name="user_query", through='MessagePushUser',
                           through_fields=('message_push', 'user'))

    class Meta:
        verbose_name = 'Announcement'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.title}"


class MessagePushUser(models.Model):
    message_push = ForeignKey(MessagePush, on_delete=CASCADE, db_constraint=False,
                              related_name="messagepushuser_message_push",
                              verbose_name='notification', help_text='notification')

    user = ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=CASCADE, db_constraint=False,
                      related_name="messagepushuser_user",
                      verbose_name='user', help_text='user')
    is_read = BooleanField(default=False, verbose_name="Have you read")
    update_datetime = UpdateDateTimeField()
    create_datetime = CreateDateTimeField()

    class Meta:
        verbose_name = "Notice Announcement and User Relationship"
        verbose_name_plural = verbose_name
