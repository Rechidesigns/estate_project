from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Message_Serializer
from inmessages.models import Estate_Messages
from rest_framework.generics import  CreateAPIView, ListCreateAPIView , ListAPIView

class Send_Message_View( ListCreateAPIView ):

    serializer_class = Message_Serializer

    def get ( self, request , *args, **kwargs ):
        qs = Estate_Messages.objects.all() #filter by benefector
        serializer = Message_Serializer(qs , many = True)
        return Response( {'status':'successful', 'message':'all messages has been fetched','data':serializer.data } , status=status.HTTP_202_ACCEPTED )

    def post (self, request, *args, **kwargs ):
        serializer = self.serializer_class( data = request.data )
        if serializer.is_valid():
            
            serializer.save(
                recipients = request.user ,
                # benefactor = request.user,
                active = True ,
                )
            return Response({'status':'successful','message':'message sent', 'data':serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response({'status':'error', 'message':'message failed to send'}, serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


# request.user

    


