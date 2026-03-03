from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'author__email',
        'published_date',
        'is_published',
        'word_count',
        'short_content'
    ]
    list_filter = ['is_published', 'published_date', 'author']
    search_fields = ['title', 'content']
    ordering = ['-published_date']
    date_hierarchy = 'published_date'

    def short_content(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content

    short_content.short_description = 'Content'