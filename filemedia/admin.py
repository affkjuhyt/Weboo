from django.contrib import admin

from filemedia.models import File, Video


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'posts', 'file')
    search_fields = ['id']
    raw_id_fields = []
    list_filter = ['posts']


admin.site.register(File, FileAdmin)


class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'posts', 'video')
    search_fields = ['id']
    raw_id_fields = []
    list_filter = ['posts']


admin.site.register(Video, VideoAdmin)
