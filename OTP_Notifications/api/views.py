import random
import string
from django.utils import timezone
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import OTP_NotificationsSerializer
from OTP_Notifications.tasks import send_otp_email_func
from OTP_Notifications.models import OTP

def otp_pin_generator():
    return ''.join(random.choices(string.digits, k=6))


class OTP_View( CreateAPIView ):
    permission_classes = [ AllowAny, ]
    serializer_class = OTP_NotificationsSerializer
    queryset = OTP.objects.all()

    def post (self, request, *args, **kwargs ):
        serializer = self.serializer_class( data = request.data )
        if serializer.is_valid():

            email = serializer.validated_data.get('email')
            otp_pin = otp_pin_generator()

            verify = self.get_queryset().filter( email = email )
            if verify.exists():
                # deleting the old otp
                verify.delete()
            # send otp to the user email address
            send_otp_email_func( email = email, otp_pin = otp_pin )
            # save the validated data
            serializer.save( otp_pin = otp_pin )

            return Response({"status":"successful", "message": "otp has been sent to the user email address successfully", "data":serializer.data}, status= status.HTTP_201_CREATED)
        
        return Response(serializer.error_messages, status= status.HTTP_400_BAD_REQUEST)
    



class OTP_Verification_View ( ListAPIView ):
    
    permission_classes = [ AllowAny, ]
    serializer_class = OTP_NotificationsSerializer
    queryset = OTP.objects.all()

    def get (self, request, *args, **kwargs):
        email = kwargs.get('email')
        otp_pin = kwargs.get('otp_pin')
        recent_time = timezone.now()

        verify = self.get_queryset().filter( email = email, otp_pin = otp_pin, active = True )
        if verify.exists():
                # check for the pin duration
                # recent_time = timezone.now()
                # for loop to get the pin duration
            for v in verify:
                pin_duration = v.pin_duration
                    # checking the recent time and oin duratuion
                if recent_time > pin_duration:
                        # delete the old otp oin
                    verify.delete()
                        # returning the response
                    return Response({"status": "error", "message":"otp is not vakid or has expired, kindly request for another pin"}, status= status.HTTP_404_NOT_FOUND)
                else:
                        # delete the old otp pin
                    verify.delete()
                        # returning the response
                    return Response({"status": "success", "message":"otp is valid"}, status= status.HTTP_201_CREATED)
                    
        return Response({"status": "error", "message":"otp or email is not valid"}, status= status.HTTP_400_BAD_REQUEST)


