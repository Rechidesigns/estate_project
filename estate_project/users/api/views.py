from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny , IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import Account_Creation
# from .serializers import User_KYC_Serializer
from estate_project.users.models import User


class Register_Account ( CreateAPIView ) :
    
    """
    this is the endpoint for account creation , which includes 
    the landlord and tenant information
    """
    permission_classes = [ AllowAny, ]
    serializer_class = Account_Creation

    def post (self, request , *args, **kwargs ):
        serializer = self.serializer_class( data = request.data )

        if serializer.is_valid():
            serializer.save(request)
            # return response
            return Response( {'status':'successful', 'message':'your account is created succesfully', 'data':serializer.data } , status = status.HTTP_201_CREATED )

        return Response( {'status':'error', 'message':'check your input and try again',} , status = status.HTTP_400_BAD_REQUEST )




    def get_tenants_for_landlord(request, landlord_id):
    # Retrieve the landlord object
        landlord = get_object_or_404(Landlord, id=landlord_id)
    
    # Retrieve all the tenants for the landlord
        tenants = Tenant.objects.filter(landlord=landlord)
    
    # Return the tenants to the template
        return render(request, 'your_template.html', {'tenants': tenants})



# class KYC_View( CreateAPIView ):

#     permission_classes = [ AllowAny, ]
#     serializer_class = User_KYC_Serializer

#     def post (self, request , *args, **kwargs ):
#         serializer = self.serializer_class( data = request.data )

#         if serializer.is_valid():
#             serializer.save(request)
#             # return response
#             return Response( {'status':'successful', 'message':'your KYC informations has been created succesfully', 'data':serializer.data } , status = status.HTTP_201_CREATED )

#         return Response( {'status':'error', 'message':'check your input and try again',} , status = status.HTTP_400_BAD_REQUEST )



