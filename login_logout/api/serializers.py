from rest_framework import serializers
from estate_project.users.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework import serializers


# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

#     def validate(self, attrs):
#         email = attrs.get('email').lower()
#         password = attrs.get('password')

#         if not email or not password:
#             raise serializers.ValidationError("Please give both email and password.")

#         if not User.objects.filter( email=email ).exists():
#             raise serializers.ValidationError('Email does not exist.')

#         user = authenticate(request=self.context.get('request'), email=email,
#                             password=password)
#         if not user:
#             raise serializers.ValidationError("Wrong Credentials.")

#         attrs['user'] = user
#         return attrs


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
