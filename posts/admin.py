from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'dateCreation', 'likes_count')
    list_filter = ('dateCreation', 'user')
    search_fields = ('title', 'description', 'user__email')
    date_hierarchy = 'dateCreation'
