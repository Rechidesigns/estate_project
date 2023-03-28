
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from estate_project.users.models import User
from rest_framework import serializers




class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)