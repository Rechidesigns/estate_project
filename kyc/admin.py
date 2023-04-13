from django.contrib import admin
from .models import Kyc

# Register your models here.
@admin.register(Kyc)
class KycApplication( admin.ModelAdmin):
    list_display = ('user_detail', 'legal_first_name', 'legal_last_name', 'country', 'state')
    list_display_links = ('user_detail', 'legal_first_name', 'legal_last_name', 'country', 'state')
    pass
    def has_add_permission(self, request):
        return False
    

