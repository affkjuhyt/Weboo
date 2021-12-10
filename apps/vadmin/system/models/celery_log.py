from django.db.models import CharField, BooleanField, TextField

from apps.vadmin.op_drf.models import CoreModel


class CeleryLog(CoreModel):
    name = CharField(max_length=256, verbose_name='mission name', help_text='mission name')
    func_name = CharField(max_length=256, verbose_name='Execution function name', help_text='Execution function name')
    kwargs = TextField(max_length=1024, verbose_name='Execution parameters', help_text='Execution parameters')
    seconds = CharField(max_length=8, verbose_name='Execution time')
    status = BooleanField(default=False, verbose_name='Operating status')
    result = TextField(max_length=10240, verbose_name='Task result', help_text='Task return content')

    class Meta:
        verbose_name = 'celery'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.creator and self.creator.name}"
