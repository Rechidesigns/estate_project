from django.contrib import admin
from .models import OTP
# Register your models here.


@admin.register( OTP )
class OTPAdmin (admin.ModelAdmin):
    list_display = ('email', 'otp_pin' )
    list_display_links = ('otp_pin',)

