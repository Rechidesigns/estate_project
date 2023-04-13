from django.contrib import admin

from .models import Maintenance

# import admin
@admin.register( Maintenance )
class MaintenanceAdmin (admin.ModelAdmin):
    list_display = ('tenant','maintenance_type','issue','description','action','status','action_date') 
    list_display_links = ('maintenance_type', 'issue', 'description')

