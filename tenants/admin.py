from django.contrib import admin

# Register your models here.
from .models import Tenant



@admin.register( Tenant )
class TenantAdmin (admin.ModelAdmin):
    list_display = ('properties' , 'created_date' , 'modified_date')
    list_display_links = [ 'properties' ]
