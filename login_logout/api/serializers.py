from rest_framework import serializers
from estate_project.users.api.serializers import User

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)



class LogoutSerializer(serializers.Serializer):
    pass
