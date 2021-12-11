import django_filters
from django.contrib.auth import get_user_model

from apps.vadmin.permission.models import Menu, Dept, Role
from apps.vadmin.util.model_util import get_dept

UserProfile = get_user_model()


class MenuFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Menu
        exclude = ('description', 'creator', 'modifier')


class DeptFilter(django_filters.rest_framework.FilterSet):
    deptName = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Dept
        exclude = ('description', 'creator', 'modifier')


class RoleFilter(django_filters.rest_framework.FilterSet):
    roleName = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Role
        exclude = ('description', 'creator', 'modifier')


# class UserProfileFilter(django_filters.rest_framework.FilterSet):
#     username = django_filters.CharFilter(lookup_expr='icontains')
#     mobile = django_filters.CharFilter(lookup_expr='icontains')
#     deptId = django_filters.CharFilter(method='filter_deptId')
#
#     def filter_deptId(self, queryset, name, value):
#         return queryset.filter(dept__id__in=get_dept(dept_id=value))
#
#     class Meta:
#         model = UserProfile
#         exclude = ('secret', 'password', 'avatar')