from django.contrib import admin

from post.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post', 'comment_text']
