from django.contrib import admin
from book.models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'text', 'status', 'created_at', 'updated_at')
    list_filter = ('id', 'name', 'email', 'text', 'status', 'created_at', 'updated_at')
    search_fields = ('id', 'name')


admin.site.register(Book, BookAdmin)
