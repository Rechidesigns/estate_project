from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Kyc_Serializer
from kyc.models import Kyc
from rest_framework.generics import  CreateAPIView, ListCreateAPIView , ListAPIView
from recuity.users.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated




class Kyc_View ( CreateAPIView ):
    permission_classes = [ IsAuthenticated, ]
    serializer_class = Kyc_Serializer



    def post ( self, request , *args, **kwargs ):

        serializer = self.serializer_class( data = request.data )

        if serializer.is_valid ():
            serializer.save()

            return Response({'status':'successful', 'message':'KYC has been uploaded successful','data':serializer.data} , status = status.HTTP_201_CREATED )

        return Response(serializer.error_messages, status = status.HTTP_400_BAD_REQUEST)


    # def post (self, request , *args, **kwargs ):  
    #     serializer = self.serializer_class( data = request.data )

    #     if serializer.is_valid( raise_exception=True ):
    #         user = User.objects.get( user_detail = request.user )
    #         try:
    #             obj = Kyc.objects.get( user_detail = request.user )
    #             return Response({ "status": "faild", "message":"User already submited KYC"}, status=400)
    #         except Kyc.DoesNotExist:
    #             serializer.save( user_detail = request.user )
    #             return Response( {'status':'successful', 'message':'KYC sent for review successfully', 'data':serializer.data } , status = status.HTTP_201_CREATED )

    #     return Response( {'status':'error', 'message':'check your input and try again',} , status = status.HTTP_400_BAD_REQUEST )


    def get ( self, request , *args, **kwargs ):
        qs = Kyc.objects.filter( )
        serializer = Kyc_Serializer(qs , many = True)
        return Response( {'status':'successful', 'message':'Kyc details has been fetched','data':serializer.data } , status=status.HTTP_201_CREATED )




class Kyc_Detail_View( APIView ): 

    permission_classes = [ IsAuthenticated, ]
    serializer_class = Kyc_Serializer
    """
    API view to handle PUT and DELETE requests for a single Property instance.
    """
    def get_object( self, kyc_id ):
      
        kyc = get_object_or_404 (Kyc, id = kyc_id )
        return kyc
       

    def get (self, request, kyc_id ):
        kyc = self.get_object( kyc_id )        
        serializer = self.serializer_class( kyc )
        return Response({'status':'successful','message':'the detail information about the kyc','data':serializer.data }, status = status.HTTP_200_OK )

    def put(self, request, kyc_id, format=None):
        kyc = self.get_object( kyc_id )
        serializer = Kyc_Serializer( kyc, data=request.data )
        if serializer.is_valid():
            serializer.save( )
            return Response({'status':'successful', 'message':'the details of the kyc has been updated'}, status = status.HTTP_200_OK)
        return Response({'status':'fail'},serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, kyc_id, format=None):
        kyc = self.get_object( kyc_id )
        kyc.delete()
        return Response({'status':'successful','message':'the kyc has been deleted successful','data':[] }, status = status.HTTP_200_OK )
    
