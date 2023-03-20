from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import  CreateAPIView, ListCreateAPIView , ListAPIView
from rest_framework.exceptions import NotFound, PermissionDenied
from .serializers import Property_Serializer,Comment_Serializer, Property_Type_Serializer , Appliances_Serializer, Parking_Type_Serializer, Utilities_Serializer,OutDoor_Spaces_Serializer,Other_Amenities_Serializer , List_Property_Serializer
from django.http import Http404
# import get_object_or_404()
from rest_framework import permissions, filters
from estate_project.users.models import User
from estate_project.users.api.serializers import UserSerializer
from django.shortcuts import get_object_or_404
from properties.models import Properties, Comments, Other_Amenities , OutDoor_Spaces , Utilities , Parking_Type , Property_Type, Appliances
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter




class Property_Options_ViewSet ( ListAPIView ):

    permission_classes = [ AllowAny, ]
    serializer_class = Property_Type_Serializer 
    
    def get (self, request, *args, **kwargs):

        property_type = Property_Type.objects.filter(active = True )
        parking_type = Parking_Type.objects.filter(active = True )
        utilities = Utilities.objects.filter(active = True )
        outDoor_spaces = OutDoor_Spaces.objects.filter(active = True )
        other_amenities = Other_Amenities.objects.filter(active = True )
        appliances = Appliances.objects.filter(active = True )

        # serialization 
        property_type_serializer = Property_Type_Serializer(property_type , many=True)
        parking_type_serializer = Parking_Type_Serializer(parking_type , many=True)
        utilities_serializer = Utilities_Serializer(utilities , many=True)
        outDoor_spaces_serializer = OutDoor_Spaces_Serializer( outDoor_spaces , many=True)
        other_amenities_serilizer = Other_Amenities_Serializer( other_amenities , many=True )
        appliances_serializer = Appliances_Serializer(appliances, many=True)

        data = {
            'property_type':property_type_serializer.data ,
            'parking_type':parking_type_serializer.data,
            'utilities':utilities_serializer.data,
            'outDoor_spaces':outDoor_spaces_serializer.data,
            'other_amenities':other_amenities_serilizer.data,
            'appliances':appliances_serializer.data,
            }

        return Response( {'status':'successful', 'message':'this consists of all the property option type that is available on the database' , 'data':data }, status = status.HTTP_200_OK)




class Properties_View ( ListCreateAPIView ):
    
    permission_classes = [ IsAuthenticated ]
    queryset = Properties.objects.all()
    serializer_class = Property_Serializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['country','state','city','number_of_storeys','number_of_bedroom_and_bathroon',]
    search_fields = ['country','state','city','number_of_storeys','number_of_bedroom_and_bathroon',]


    def post ( self, request , *args, **kwargs ):
        serializer = self.serializer_class( data = request.data )
        if serializer.is_valid ():
            serializer.save( Landlord = request.user )
            return Response( {'status':'successful', 'message':'property has been uploaded successful','data':serializer.data} , status = status.HTTP_201_CREATED )

        return Response(serializer.error_messages, status = status.HTTP_400_BAD_REQUEST)



    def get ( self, request , *args, **kwargs ):
        qs = Properties.objects.all()
        serializer = List_Property_Serializer(qs , many = True)
        return Response( {'status':'successful', 'message':'landlord properties has been fetched','data':serializer.data } , status=status.HTTP_201_CREATED )



class Property_Detail_View( APIView ): 

    permission_classes = [ IsAuthenticated, ]
    serializer_class = Property_Serializer
    """
    API view to handle PUT and DELETE requests for a single Property instance.
    """
    def get_object( self, property_id ):
      
        property = get_object_or_404 (Properties, id = property_id )
        return property
       

    def get (self, request, p_id ):
        property = self.get_object( p_id )        
        serializer = self.serializer_class( property )
        return Response({'status':'successful','message':'the detail information about the property','data':serializer.data }, status = status.HTTP_200_OK )

    def put(self, request, p_id, format=None):
        property = self.get_object( p_id )
        serializer = Property_Serializer( property, data=request.data )
        if serializer.is_valid():
            serializer.save( )
            return Response({'status':'successful', 'message':'the details of the property has been updated'}, status = status.HTTP_200_OK)
        return Response({'status':'fail'},serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, p_id, format=None):
        property = self.get_object( p_id )
        property.delete()
        return Response({'status':'successful','message':'the property has been deleted successful','data':[] }, status = status.HTTP_200_OK )
    


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


# class Properties_List(ListAPIView):
#     queryset = Properties.objects.all()
#     serializer_class = Property_Serializer
#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     filter_fields = ['id','country','state','city','number_of_storeys','number_of_bedroom_and_bathroon',]
#     search_fields = ['id','address_1','country','state','city','amount','number_of_unit', 'appliances', 'property_type','unit_number','number_of_storeys','number_of_bedroom_and_bathroon']

