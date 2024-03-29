
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import  CreateAPIView, ListCreateAPIView , ListAPIView
from rest_framework.exceptions import NotFound, PermissionDenied
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.core.mail import send_mail
from .serializers import None_Rented_Properties
from tenants.models import Tenant
from properties.models import Properties




class All_Free_Property_View( APIView ):
    permission_classes = [ IsAuthenticated, ]
    serializer_class = None_Rented_Properties

    def get ( self, request, *args, **kwargs ):
        # checking for the user account type 
        if request.user.account_type == "Landlord":
            qs = Tenant.objects.filter ( landlord = request.user )
        elif request.user.account_type == "Tenant":
            qs = Tenant.objects.filter ( status = False )
        else:
            return Response({'status':'error', 'message':'Invalid account or not allowed to make this request'}, status=status.HTTP_403_FORBIDDEN )

        serializer = self.serializer_class( qs , many=True )
        return Response({'status':'successful', 'message':'this is the list of the property that is available', 'data':serializer.data}, status=status.HTTP_200_OK )
        



class Rent_Property_View( APIView ):
    """
    this function store the property renting action which
    meant to taken by the tenants only.
    """
    permission_classes = [ IsAuthenticated, ]
    serializer_class = None_Rented_Properties
    rent_qs = Tenant.objects.all()

    def post ( self, request, property_id ):
        try:
            landlord_property = Properties.objects.get( id = property_id )

        except Properties.DoesNotExist:
            return Response({'status':'error', 'message': 'Property can not be found in our database.'}, status = status.HTTP_404_NOT_FOUND )


        # checking if the property is already been processed by the tenant
        checking_rent_by_user = self.rent_qs.filter( properties_id = property_id )
        
        for t in checking_rent_by_user:
            if t.user == request.user:
                return Response({'status':'error', 'message': 'Renting property is already been process by you, kindly cancel or wait for the landlord action.'}, status = status.HTTP_404_NOT_FOUND )

            elif t.action == "rented":
                return Response({'status':'error', 'message': 'Property has been rented out by the landlord'}, status = status.HTTP_404_NOT_FOUND )
            
            else:
                pass

        rent_property = Tenant()
        rent_property.user = request.user # this is the tenant account
        rent_property.landlord = landlord_property.landlord # this is the landlord account
        rent_property.properties = landlord_property # this is the landlord property profile
        rent_property.action = "processing" # this is the property status
        rent_property.status = False
        rent_property.action_date = timezone.now() #this stores the action timestamp
        rent_property.save() #this saves the rental process


        # sending email to the property owner - email notification
        send_mail(
            ' Property Rent Notification ',
            f'Hey Landlord, kindly check your rechi property dashboard , you currently have a tenant that wants to rent your listed property',
            # tenant email here 
            request.user.email,
            # landlord email here
            [landlord_property.landlord.email],
            fail_silently = False,
        )
    
        return Response({'status':'successfull', 'message': 'the property rent process is been submited for review'}, status = status.HTTP_200_OK)
    

    def patch ( self, request, property_id ):
        all_my_properties = Tenant.objects.get( id = property_id, landlord = request.user )
        all_my_properties.action = "processing"
        all_my_properties.status = False
        all_my_properties.action_date = timezone.now()
        all_my_properties.save()

        return Response({ 'status':'successfull', 'message': 'the property has been updated' }, status = status.HTTP_200_OK )








