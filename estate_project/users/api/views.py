from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny , IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import Account_Creation
# from .serializers import Applicant_Information_KYC_Serializer
from estate_project.users.models import User
# from estate_project.users.models import Applicant_Information
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework import status




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




    # def get_tenants_for_landlord(request, landlord_id):
    # # Retrieve the landlord object
    #     landlord = get_object_or_404(Landlord, id=landlord_id)
    
    # # Retrieve all the tenants for the landlord
    #     tenants = Tenant.objects.filter(landlord=landlord)
    
    # # Return the tenants to the template
    #     return render(request, 'your_template.html', {'tenants': tenants})



# class Applicant_Information_KYC_View( ListCreateAPIView ):

#     permission_classes = [ IsAuthenticated ]
#     serializer_class = Applicant_Information_KYC_Serializer
#     queryset = Applicant_Information.objects.filter( status = True )

#     # qs = Applicant_Information.objects.all()
#     def get(self, request):
#        kyc_details  =  Applicant_Information.objects.all()
#        serializer =  Applicant_Information_KYC_Serializer(kyc_details, many=True)
#        return Response(serializer.data)
    


#     def post (self, request , *args, **kwargs ):
#         serializer = self.serializer_class( data = request.data )

#         if serializer.is_valid():
#             serializer.save()
#             # return response
#             return Response( {'status':'successful', 'message':'your KYC informations has been created succesfully', 'data':serializer.data } , status = status.HTTP_201_CREATED )

#         return Response( {'status':'error', 'message':'check your input and try again',} , status = status.HTTP_400_BAD_REQUEST )



# class Applicant_Information_Detail_View(APIView):

#     permission_classes = [ IsAuthenticated ]
#     serializer_class = Applicant_Information_KYC_Serializer

#     def get_object( self, kyc_id ):
      
#         kyc = get_object_or_404 (Applicant_Information, id = kyc_id )
#         return kyc


#     def get (self, request, kyc_id ):
#         kyc = self.get_object( kyc_id )        
#         serializer = self.serializer_class( kyc )
#         return Response({'status':'successful','message':'the detail information about the property','data':serializer.data }, status = status.HTTP_200_OK )



