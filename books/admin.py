from django.contrib import admin
from .models import Book, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['user', 'book', 'text', 'datetime_created', 'recommend']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'author', 'cover']
# admin.site.register(Comment, CommentAdmin)
