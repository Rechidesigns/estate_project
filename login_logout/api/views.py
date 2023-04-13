import json
from jsonschema import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from estate_project.users.models import User
from estate_project.users.api.serializers import UserSerializer
from knox import views as knox_views
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout
from login_logout.api.serializers import LoginSerializer, LogoutSerializer



User = get_user_model()



# class LoginAPIView(knox_views.LoginView):
#     permission_classes = (AllowAny, )
#     serializer_class = LoginSerializer

#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             user = serializer.validated_data['user']
#             login(request, user)
#             response = super().post(request, format=None)
#         else:
#             return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#         return Response(response.data, status=status.HTTP_200_OK)





class LoginView(APIView):
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token)})
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)





class LogoutView(APIView):
    serializer_class = LogoutSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        logout(request)

        return Response({'detail': 'Successfully logged out'})
