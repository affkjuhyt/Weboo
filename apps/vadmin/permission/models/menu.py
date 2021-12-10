from django.core.cache import cache
from django.db.models import IntegerField, ForeignKey, CharField, CASCADE, Q

from root import settings
from apps.vadmin.op_drf.models import CoreModel


class Menu(CoreModel):
    parentId = ForeignKey(to='Menu', on_delete=CASCADE, verbose_name="parentId", null=True, blank=True, db_constraint=False)
    menuType = CharField(max_length=8, verbose_name="menuType")
    icon = CharField(max_length=64, verbose_name="icon", null=True, blank=True)
    name = CharField(max_length=64, verbose_name="name")
    orderNum = IntegerField(verbose_name="orderNum")
    isFrame = CharField(max_length=8, verbose_name="isFrame")
    web_path = CharField(max_length=128, verbose_name="Web path", null=True, blank=True)
    component_path = CharField(max_length=128, verbose_name="Component path", null=True, blank=True)
    interface_path = CharField(max_length=256, verbose_name="Interface path", null=True, blank=True)
    interface_method = CharField(max_length=16, default='GET', verbose_name="interface method")
    perms = CharField(max_length=256, verbose_name="perms", null=True, blank=True)
    status = CharField(max_length=8, verbose_name="status")
    visible = CharField(max_length=8, verbose_name="visible")
    isCache = CharField(max_length=8, verbose_name="isCache")

    @classmethod
    def get_interface_dict(cls):
        try:
            interface_dict = cache.get('permission_interface_dict', {}) if getattr(settings, "REDIS_ENABLE",
                                                                                   False) else {}
        except:
            interface_dict = {}
        if not interface_dict:
            for ele in Menu.objects.filter(~Q(interface_path=''), ~Q(interface_path=None), status='1', ).values(
                    'interface_path', 'interface_method'):
                if ele.get('interface_method') in interface_dict:
                    interface_dict[ele.get('interface_method', '')].append(ele.get('interface_path'))
                else:
                    interface_dict[ele.get('interface_method', '')] = [ele.get('interface_path')]
            if getattr(settings, "REDIS_ENABLE", False):
                cache.set('permission_interface_dict', interface_dict, 84600)
        return interface_dict

    @classmethod
    def delete_cache(cls):
        if getattr(settings, "REDIS_ENABLE", False):
            cache.delete('permission_interface_dict')

    class Meta:
        verbose_name = 'Quản lý menu'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name}"
