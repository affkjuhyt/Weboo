from django.contrib import admin

from userprofile.models import UserProfile, FollowBook, DownLoadBook


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'email', 'full_name', 'user_type', 'coin']
    search_fields = ['full_name', 'email']
    raw_id_fields = ['user']


admin.site.register(UserProfile, UserProfileAdmin)


class FollowBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'book', 'status']
    search_fields = ['user', 'book']
    raw_id_fields = ['user']


admin.site.register(FollowBook, FollowBookAdmin)


class DownloadAdmin(admin.ModelAdmin):
    list_display = ['id', 'chapter', 'user', 'status']
    search_fields = ['user', 'chapter']
    raw_id_fields = ['user']


admin.site.register(DownLoadBook, DownloadAdmin)
