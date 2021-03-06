from django.contrib import admin

from apps.vadmin.permission.models import Menu, Role, UserProfile


class MenusAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'parentId', 'menuType', 'icon', 'name', 'orderNum', 'isFrame', 'web_path', 'component_path',
        'interface_path', 'interface_method', 'perms', 'status', 'visible', 'isCache')
    search_fields = ['title', 'author']
    raw_id_fields = []
    list_filter = ['parentId', 'orderNum', 'status']


class RolesAdmin(admin.ModelAdmin):
    list_display = ('id', 'roleName', 'roleKey', 'roleSort', 'status')
    search_fields = ['roleName']
    raw_id_fields = []


class UserProfilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name', 'gender', 'user_type')
    search_fields = ['name']
    raw_id_fields = []
    list_filter = ['gender', 'user_type']


admin.site.register(UserProfile, UserProfilesAdmin)
admin.site.register(Role, RolesAdmin)
admin.site.register(Menu, MenusAdmin)
