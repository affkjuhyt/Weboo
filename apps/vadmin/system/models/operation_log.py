from django.db.models import TextField, CharField, BooleanField

from apps.vadmin.op_drf.models import CoreModel


class OperationLog(CoreModel):
    request_modular = CharField(max_length=64, verbose_name="Request module", null=True, blank=True)
    request_path = CharField(max_length=400, verbose_name="Request address", null=True, blank=True)
    request_body = TextField(verbose_name="Request parameter", null=True, blank=True)
    request_method = CharField(max_length=64, verbose_name="Request method", null=True, blank=True)
    request_msg = TextField(verbose_name="Instructions", null=True, blank=True)
    request_ip = CharField(max_length=32, verbose_name="Request Ip", null=True, blank=True)
    request_browser = CharField(max_length=64, verbose_name="Request browser", null=True, blank=True)
    response_code = CharField(max_length=32, verbose_name="Request code", null=True, blank=True)
    request_location = CharField(max_length=64, verbose_name="Request location", null=True, blank=True)
    request_os = CharField(max_length=64, verbose_name="Request Os", null=True, blank=True)
    json_result = TextField(verbose_name="Returned messages", null=True, blank=True)
    status = BooleanField(default=False, verbose_name="Status")

    class Meta:
        verbose_name = 'Operation log'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.request_msg}[{self.request_modular}]"
