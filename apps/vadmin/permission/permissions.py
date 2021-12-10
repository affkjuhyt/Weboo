import logging

from django.contrib.auth import get_user_model
from rest_framework.permissions import (BasePermission,
                                        )
from rest_framework.request import Request
from rest_framework.views import APIView

from apps.vadmin.permission.models import Dept
from apps.vadmin.util.model_util import get_dept

logger = logging.getLogger(__name__)
User = get_user_model()


class CustomPermission(BasePermission):
    def __init__(self, message=None) -> None:
        super().__init__()
        self.message = getattr(self.__class__, 'message', '无权限')
        self.user: User = None

    def init_permission(self, request: Request, view: APIView):
        self.user = request.user

    def has_permission(self, request: Request, view: APIView):
        return True

    def has_object_permission(self, request: Request, view: APIView, obj):
        return True


class CommonPermission(CustomPermission):
    message = '没有有操作权限'

    def check_queryset(self, request, instance):
        user_dept_id = getattr(request.user, 'dept_id')
        if not user_dept_id:
            self.message = "该用户无部门，无权限操作！"
            return False

        if not getattr(instance, 'dept_belong_id', None):
            return True

        if not hasattr(request.user, 'role'):
            self.message = "该用户无角色，无权限操作！"
            return False

        role_list = request.user.role.filter(status='1').values('admin', 'dataScope')
        dataScope_list = []
        for ele in role_list:
            if '1' == ele.get('dataScope') or ele.get('admin') == True:
                return True
            dataScope_list.append(ele.get('dataScope'))
        dataScope_list = list(set(dataScope_list))

        if dataScope_list == ['5']:
            return int(instance.dept_belong_id) == user_dept_id and request.user == instance.creator

        dept_list = []
        for ele in dataScope_list:
            if ele == '2':
                dept_list.extend(request.user.role.filter(status='1').values_list('dept__id', flat=True))
            elif ele == '3':
                dept_list.append(user_dept_id)
            elif ele == '4':
                dept_list.extend(get_dept(user_dept_id, ))
        return int(instance.dept_belong_id) in list(set(dept_list))

    def has_permission(self, request: Request, view: APIView):
        return True

    def has_object_permission(self, request: Request, view: APIView, instance):
        self.message = f"没有此数据操作权限!"
        res = self.check_queryset(request, instance)
        return res


class DeptDestroyPermission(CustomPermission):
    message = '没有有操作权限'

    def has_permission(self, request: Request, view: APIView):
        return True

    def check_queryset(self, request, instance):
        if list(filter(None, instance.values_list('userprofile', flat=True))):
            self.message = "该部门下有关联用户，无法删除！"
            return False
        if Dept.objects.filter(parentId__in=instance).count() > 0:
            self.message = "该部门下有下级部门，请先删除下级部门！"
            return False
        return True

    def has_object_permission(self, request: Request, view: APIView, instance):
        res = self.check_queryset(request, instance)
        return res
