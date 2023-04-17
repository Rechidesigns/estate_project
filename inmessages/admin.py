from django.contrib import admin

from .models import Estate_Messages
# Register your models here.

@admin.register( Estate_Messages )
class Estate_MessagesAdmin (admin.ModelAdmin):
    list_display = ('message_type', 'sender', 'recipients', 'subject_heading', 'message_content', 'created_date' , 'modified_date')
    list_display_links = ('recipients' ,'sender', 'subject_heading', 'message_content' )

