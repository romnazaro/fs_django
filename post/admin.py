from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from post.models import *


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text_min', 'text')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created', 'moderation')


admin.site.register(Comments, CommentAdmin)
