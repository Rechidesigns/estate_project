

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import  CreateAPIView, ListCreateAPIView , ListAPIView
from rest_framework.exceptions import NotFound, PermissionDenied
from django.http import Http404
from django.shortcuts import get_object_or_404
from .serializers import Tenant_Serializer
from tenants.models import Tenant
from properties.models import Properties
from django.utils import timezone
from django.core.mail import send_mail



# class Tenant_View( ListCreateAPIView ):

#     permission_classes = [ IsAuthenticated ]
#     serializer_class = Tenant_Serializer


class Rent_Property_View( APIView ):

    permission_classes = [ IsAuthenticated, ]

    def get ( self, request, property_id ):
        # timezone.now()
        try:
            landlord_property = Properties.obejcts.get( id = property_id )
        except Properties.DoesNotExist:
            return Response({'status':'property not found', 'message': 'Property can not be found'}, status = status.HTTP_404_NOT_FOUND)


    def post ( self, request, property_id ):

        landlord_property = Properties

        rent_property = Tenant()
        rent_property.user = request.user
        rent_property.landlord = landlord_property.landlord
        rent_property.property = landlord_property
        rent_property.action = "processing"
        rent_property.status = False
        rent_property.action_date = timezone.now()
        rent_property.save()

        send_mail(
            ' Property Rent Notification ',
            f'Hey { landlord_property.landlord.name }, kindly check your rechi property dashboard , you currently have a tenant that wants to rent your listed property',
            # tenant email here 
            'request.user.email',
            # landlord email here
            ['landlord_property.landlord'],
            fail_silently=False,
        )
    
        return Response({'status':'successfull', 'message': 'the listed property is been processing state'}, status = status.HTTP_200_OK)


        # landlord section 
    def get_method (request, id ): 
        Tenant.objects.filter( landlord = request.user ) 
        Tenant.objects.get( id = id , landlord = request.user )
        
        # {
        # status = successful
        #     message =  ' list of all the properties that has renting request '
        #     data = {
        #         'user':{
        #                 'full_name':'michael asa',
        #                 'phone_number':'09876543456',
        #                 'address':'no 45 tony umeh ph street'
        #             }
        #         'action':'processing'
        #         'status':'false'
        #         'action_date':'12-03-2024-12-23-2'
        #     }
        # }
        




    def put ( self, request, id ):
        
        all_my_properties = Tenant.objects.get( id = id , landlord = request.user )
        all_my_properties.action = "processing"
        all_my_properties.status = False
        all_my_properties.action_date = timezone.now()
        all_my_properties.save()
        






"""
        try:
            landlord_property = Property.obejcts.get( id = property_id )
        except Property.DoesNotExist:
            return Response({'status':'property not found'})

        rent_property = Tenant()
        rent_property.user = request.user
        rent_property.landlord = landlord_property.landlord
        rent_property.property = landlord_property
        rent_property.action = "processing"
        rent_property.status = False
        rent_property.action_date = timezone.now()
        rent_property.save()


        # sending email to the landlord 

        from django.core.mail import send_mail

        send_mail(
            ' Property Rent Notification ',
            f'Hey { landlord_property.landlord.name }, kindly check your rechi property dashboard , you currently have a tenant that wants to rent your listed property',
            # tenant email here 
            'request.user.email',
            # landlord email here
            ['landlord_property.landlord'],
            fail_silently=False,
        )
        
        return response -- the listed property is been processing state 


        # landlord section 
        get method request = all properties ..... Tennats.objects.filter( landlord = request.user )
        get method request by PROPERTY ID  = get the property by PROPERTY ID ... Tennats.objects.get( id = id , landlord = request.user )
        
        {
            status = successful
            message =  ' list of all the properties that has renting request '
            data = {
                'user':{
                        'full_name':'michael asa',
                        'phone_number':'09876543456',
                        'address':'no 45 tony umeh ph street'
                    }
                'action':'processing'
                'status':'false'
                'action_date':'12-03-2024-12-23-2'
            }
        }

        patch method request =  PROPERTY ID 
        all_my_properties = Tennats.objects.get( id = id , landlord = request.user )
        all_my_properties.action = "processing"
        all_my_properties.status = False
        all_my_properties.action_date = timezone.now()
        all_my_properties.save()

            

"""
        
