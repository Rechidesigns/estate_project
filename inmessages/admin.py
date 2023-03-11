from django.contrib import admin

from .models import Estate_Messages
# Register your models here.

@admin.register( Estate_Messages )
class Estate_MessagesAdmin (admin.ModelAdmin):
    list_display = ('message_type', 'recipients', 'subject', 'body', 'created_date' , 'modified_date')
    list_display_links = ('recipients' , 'subject', 'body' )