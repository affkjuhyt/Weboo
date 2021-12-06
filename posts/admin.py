from django.contrib import admin

from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'group', 'content', 'like_count', 'share_count')
    search_fields = ['user']
    raw_id_fields = []


admin.site.register(Post, PostAdmin)
