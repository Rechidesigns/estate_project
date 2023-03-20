from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Message_Serializer
from inmessages.models import Estate_Messages
from rest_framework.generics import  CreateAPIView, ListCreateAPIView , ListAPIView
from django.core.mail import send_mail
from estate_project.users.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated


class All_messages_View(APIView):

    permission_classes = [ IsAuthenticated, ]
    serializer_class = Message_Serializer

    def get ( self, request , *args, **kwargs ):
        qs = Estate_Messages.objects.all() #filter by benefector
        serializer = Message_Serializer(qs , many = True)
        return Response( {'status':'successful', 'message':'all messages has been fetched','data':serializer.data } , status=status.HTTP_202_ACCEPTED )


class Send_Message_View( APIView ):
    permission_classes = [ IsAuthenticated, ]
    serializer_class = Message_Serializer

    def post(self, request, **kwargs):
        try:
            print(request.data)
            email = request.data.get('email')
            recipients = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'status': 'error', 'message': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            serializer.save(
                sender = request.user,
                recipients=recipients,
                active=True
                )

            send_mail(
                'Property Rent Notification',
                f'Hey {recipients.email}, kindly check your rechi property account, you have a new message',
                request.user.email,
                [recipients.email],
                fail_silently=False,
            )

            return Response({'status': 'successful', 'message': 'message sent successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# ############




# class Send_Message_View(CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = Message_Serializer

#     def post(self, request, **kwargs):
#         try:
#             recipients = User.objects.get()
#         except User.DoesNotExist:
#             return Response({'status': 'error', 'message': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)

#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():

#             message = serializer.save(recipients=recipients, active=True)

#             send_mail(
#                 'Property Rent Notification',
#                 f'Hey {recipients.first_name}, kindly check your rechi property account, you have a new message',
#                 request.user.email,
#                 [recipients.email],
#                 fail_silently=False,
#             )

#             return Response({'status': 'successful', 'message': 'message sent successful'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'status': 'error', 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
