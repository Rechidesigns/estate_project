from django.contrib import admin
from .models import Comments
# from comments.models import Comments


@admin.register( Comments )
class CommentsAdmin (admin.ModelAdmin):
    list_display = ('properties','comment') 
    list_display_links = ('properties', 'comment')