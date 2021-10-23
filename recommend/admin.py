from django.contrib import admin
from django_neomodel import admin as neo_admin

# Register your models here.
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "published")


neo_admin.register(Book, BookAdmin)
