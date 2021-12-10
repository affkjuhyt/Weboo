from django.db.models import CharField, ForeignKey, BooleanField, CASCADE

from apps.vadmin.op_drf.models import CoreModel


class DictDetails(CoreModel):
    dictLabel = CharField(max_length=64, verbose_name="Dictionary tag")
    dictValue = CharField(max_length=256, verbose_name="Dictionary key")
    is_default = BooleanField(verbose_name="Default", default=False)
    status = CharField(max_length=2, verbose_name="Dictionary status")
    sort = CharField(max_length=256, verbose_name="Dictionary sort")
    dict_data = ForeignKey(to='system.DictData', on_delete=CASCADE, verbose_name="Associative dictionary",
                           db_constraint=False)
    remark = CharField(max_length=256, verbose_name="Remark", null=True, blank=True)

    @classmethod
    def get_default_dictValue(cls, dictName):
        instance = DictDetails.objects.filter(dict_data__dictName=dictName, is_default=True).first()
        return instance and instance.dictValue

    class Meta:
        verbose_name = 'Dictionary details'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.dictLabel}"
