from django.contrib import admin
from .models import Author, Category, Post, Comment


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'bd', 'email']
    search_fields = ['last_name']
    search_help_text = 'Поиск по полю Фамилия (last_name)'

    readonly_fields = ['bd']
    fieldsets = [
        (None, {
            'classes': ['wide'],
            'fields': [('first_name', 'last_name'), 'bio']
        }),
        ('Личные данные', {
            'classes': ['collapse'],
            'description': 'Личные данные автора',
            'fields': ['email', 'bd'],
        })
    ]


class PostAdmin(admin.ModelAdmin):
    list_display = ['publish', 'title', 'category', 'author', 'publish_date', 'views']


class CommentAdmin(admin.ModelAdmin):
    def short_comment(self, obj):
        return obj.comment[:35] + '...' if len(obj.comment) > 35 else obj.comment

    short_comment.short_description = 'Comment'
    list_display = ['short_comment', 'publish_date']


# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
