from django.contrib import admin
from .models import Kyc

# Register your models here.
@admin.register(Kyc)
class KycApplication( admin.ModelAdmin):
    pass
    # def has_add_permission(self, request):
    #     return False