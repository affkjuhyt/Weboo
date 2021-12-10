from django.db.models import CharField, BooleanField, TextField

from apps.vadmin.op_drf.models import CoreModel


class LoginInfor(CoreModel):
    session_id = CharField(max_length=64, verbose_name="Session ID", null=True, blank=True)
    browser = CharField(max_length=64, verbose_name="Browser")
    ipaddr = CharField(max_length=32, verbose_name="ip", null=True, blank=True)
    loginLocation = CharField(max_length=64, verbose_name="Login location", null=True, blank=True)
    msg = TextField(verbose_name="Operation information", null=True, blank=True)
    os = CharField(max_length=64, verbose_name="Operating system", null=True, blank=True)
    status = BooleanField(default=False, verbose_name="Login status")

    class Meta:
        verbose_name = 'Login log'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.creator and self.creator.name}"
