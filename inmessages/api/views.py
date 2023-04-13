from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Message_Serializer
from inmessages.models import Estate_Messages
from rest_framework.generics import  CreateAPIView, ListCreateAPIView , ListAPIView
from django.core.mail import send_mail
from estate_project.users.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.core.exceptions import ValidationError
from django.core.validators import validate_email




class All_messages_View(APIView):

    permission_classes = [ IsAuthenticated, ]
    serializer_class = Message_Serializer

    def get ( self, request , *args, **kwargs ):
        qs = Estate_Messages.objects.all() #filter by benefector
        serializer = Message_Serializer(qs , many = True)
        return Response( {'status':'successful', 'message':'all messages has been fetched','data':serializer.data } , status=status.HTTP_202_ACCEPTED )




# class Send_Message_View ( CreateAPIView ):
#     permission_classes = [ IsAuthenticated, ]
#     serializer_class = Message_Serializer

#     def post (self, request , *args, **kwargs ):
#         serializer = self.serializer_class( data = request.data )

#         if serializer.is_valid():
#             serializer.save( )

            
#             # return response
#             return Response( {'status':'successful', 'message':'message sent successful', 'data':serializer.data } , status = status.HTTP_201_CREATED )

#         return Response( {'status':'error', 'message':'check your input and try again',} , status = status.HTTP_400_BAD_REQUEST )







class Send_Message_View(CreateAPIView):
    permission_classes = [ IsAuthenticated, ]
    serializer_class = Message_Serializer

    def post(self, request, **kwargs):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            recipient_email = serializer.validated_data.get('recipient_email')
            try:
                recipient_info = User.objects.get( email = recipient_email )
            except User.DoesNotExist:
                return Response({'status': 'error', 'message': 'Invalid or non-existent recipient email address'},status=status.HTTP_400_BAD_REQUEST)
            
            subject = 'Message notifications'
            content = 'Dear user, kindly loging your rechi site you have a message'

            serializer.save( sender = self.request.user, recipients = recipient_info, active = True, subject_heading = subject, message_content = content )

            # Send email
            send_mail(
                f'{subject}',
                f'{content}',
                request.sender.email,
                [recipient_info.email],
                fail_silently=False,
            )
    
            return Response({'status': 'successful', 'message': 'message sent successfully'}, status=status.HTTP_200_OK)
        
        else:
            return Response({'status': 'error', 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



