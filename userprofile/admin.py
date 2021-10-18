from django.contrib import admin

from userprofile.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'email', 'full_name', 'user_type', 'coin']
    search_fields = ['full_name', 'email']
    raw_id_fields = ['user']


admin.site.register(UserProfile, UserProfileAdmin)
