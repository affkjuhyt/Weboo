from django.db import models

from utils.base_models import CoreModel


class LoginInfor(CoreModel):
    session_id = models.CharField(max_length=64, null=True, blank=True)
    browser = models.CharField(max_length=64, null=True)
    ipaddr = models.CharField(max_length=32, null=True, blank=True)
    loginLocation = models.CharField(max_length=64, null=True, blank=True)
    msg = models.TextField(null=True, blank=True)
    os = models.CharField(max_length=64, null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.browser}"
