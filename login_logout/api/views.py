from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from estate_project.users.models import User
from estate_project.users.api.serializers import UserSerializer
from .serializers import  LoginSerializer
from knox import views as knox_views
from django.contrib.auth import login
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.models import Token


# User = get_user_model()



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
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                email=serializer.validated_data['email'], # Use the email field instead of username
                password=serializer.validated_data['password']
            )
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response({'message': 'Successfully logged out'})
