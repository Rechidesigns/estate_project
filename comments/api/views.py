from properties.models import Properties
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import  CreateAPIView, ListCreateAPIView , ListAPIView
from rest_framework.exceptions import NotFound, PermissionDenied
from comments.api.serializers import Comment_Serializer
from comments.models import Comments


class Comment_View ( ListCreateAPIView ):
    
    permission_classes = [ AllowAny ]
    serializer_class = Comment_Serializer


    def post ( self, request , *args, **kwargs ):
        serializer = self.serializer_class( data = request.data )
        if serializer.is_valid ():
            serializer.save( )
            return Response( {'status':'successful', 'message':'Comment has been added successful','data':serializer.data} , status = status.HTTP_201_CREATED )

        return Response(serializer.error_messages, status = status.HTTP_400_BAD_REQUEST)



    def get ( self, request , *args, **kwargs ):
        qs = Comments.objects.all()
        serializer = Comment_Serializer(qs , many = True)
        return Response( {'status':'successful', 'message':'Comments has been fetched','data':serializer.data } , status=status.HTTP_201_CREATED )

