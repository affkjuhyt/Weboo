import os
import uuid

from django.db.models import CharField, FileField, BooleanField
from django.utils import timezone

from apps.vadmin.op_drf.models import CoreModel


def files_path(instance, filename):
    return '/'.join(['system', timezone.now().strftime("%Y-%m-%d"), str(uuid.uuid4()) + os.path.splitext(filename)[-1]])


class SaveFile(CoreModel):
    name = CharField(max_length=128, verbose_name="File name", null=True, blank=True)
    type = CharField(max_length=200, verbose_name="Type", null=True, blank=True)
    size = CharField(max_length=64, verbose_name="Size", null=True, blank=True)
    address = CharField(max_length=16, verbose_name="Address", null=True, blank=True)
    source = CharField(max_length=16, verbose_name="Source", null=True, blank=True)
    oss_url = CharField(max_length=200, verbose_name="OSS", null=True, blank=True)
    status = BooleanField(default=True, verbose_name="Status")
    file = FileField(verbose_name="URL", upload_to=files_path, )

    class Meta:
        verbose_name = 'SaveFile'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name}"
