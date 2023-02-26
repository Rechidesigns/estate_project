from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import  CreateAPIView, ListCreateAPIView , ListAPIView

from .serializers import Property_Serializer, Property_Type_Serializer , Appliances_Serializer, Parking_Type_Serializer, Utilities_Serializer,OutDoor_Spaces_Serializer,Other_Amenities_Serializer , List_Property_Serializer

from properties.models import Properties , Other_Amenities , OutDoor_Spaces , Utilities , Parking_Type , Property_Type, Appliances


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
    
    permission_classes = [ IsAuthenticated , ]
    serializer_class = Property_Serializer

    def post ( self, request , *args, **kwargs ):
        serializer = self.serializer_class( data = request.data )
        if serializer.is_valid():
            serializer.save( landlord = request.user )
            return Response( {'status':'successful', 'message':'property has been uploaded successful','data':serializer.data} , status = status.HTTP_201_CREATED )

        return Response(serializer.error_messages, status = status.HTTP_400_BAD_REQUEST)


    def get ( self, request , *args, **kwargs ):
        qs = Properties.objects.all()
        serializer = List_Property_Serializer(qs , many = True)
        return Response( {'status':'successful', 'message':'landlord properties has been fetched','data':serializer.data } , status=status.HTTP_201_CREATED )

