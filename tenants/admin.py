from django.contrib import admin

# Register your models here.
from .models import Tenant



@admin.register( Tenant )
class TenantAdmin (admin.ModelAdmin):
    list_display = ('properties' ,'user', 'created_date' , 'modified_date')
    list_display_links = [ 'properties']


# @admin.register( Applicant_Information )
# class Applicant_InformationAdmin (admin.ModelAdmin):
#     list_display = ('full_name','email_address', 'contact_number')
#     list_display_links = [ 'full_name' ]
