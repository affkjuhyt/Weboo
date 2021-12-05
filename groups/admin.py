from django.contrib import admin

from groups.models import Group, GroupUser


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'post_count', 'member_count')
    search_fields = ['name']
    list_filter = ['name']


admin.site.register(Group, GroupAdmin)


class GroupUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'groups', 'user')
    search_fields = ['id']
    list_filter = ['groups']


admin.site.register(GroupUser, GroupUserAdmin)
