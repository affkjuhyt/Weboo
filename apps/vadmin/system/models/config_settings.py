from django.db.models import CharField

from apps.vadmin.op_drf.models import CoreModel


class ConfigSettings(CoreModel):
    configName = CharField(max_length=64, verbose_name="parameter name")
    configKey = CharField(max_length=256, verbose_name="Parameter key name")
    configValue = CharField(max_length=256, verbose_name="Parameter key value")
    configType = CharField(max_length=8, verbose_name="Whether built-in")
    status = CharField(max_length=8, verbose_name="Parameter status")
    remark = CharField(max_length=256, verbose_name="Remark", null=True, blank=True)

    class Meta:
        verbose_name = 'Parameter settings'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.configName}"
