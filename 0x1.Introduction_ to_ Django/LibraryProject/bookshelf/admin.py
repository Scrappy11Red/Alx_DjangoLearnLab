from django.contrib import admin

# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date")
    search_fields = ("list_filter", "publication_year")

admin.site.register(Book)