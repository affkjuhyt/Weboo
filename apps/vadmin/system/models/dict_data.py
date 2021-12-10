from django.db.models import TextField, CharField,ForeignKey

from apps.vadmin.op_drf.models import CoreModel


class DictData(CoreModel):
    dictName = CharField(max_length=64, verbose_name="Dictionary name")
    dictType = CharField(max_length=64, verbose_name="Dictionary type")
    status = CharField(max_length=8, verbose_name="Dictionary status")
    remark = CharField(max_length=256,verbose_name="Remark", null=True, blank=True)

    class Meta:
        verbose_name = 'Dictionary management'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.dictName}"
