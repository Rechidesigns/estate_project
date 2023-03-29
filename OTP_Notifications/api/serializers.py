from rest_framework import serializers

from OTP_Notifications.models import OTP

class OTP_NotificationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OTP
        fields = ['email',]