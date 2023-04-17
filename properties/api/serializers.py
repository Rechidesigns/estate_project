from rest_framework import serializers

from properties.models import Properties , Other_Amenities , OutDoor_Spaces , Utilities , Parking_Type , Property_Type, Appliances


class Property_Type_Serializer (serializers.ModelSerializer):

    class Meta:
        model = Property_Type
        fields = ['option','id',]


class Parking_Type_Serializer (serializers.ModelSerializer):

    class Meta:
        model = Parking_Type
        fields = ['option','id',]


class Utilities_Serializer (serializers.ModelSerializer):

    class Meta:
        model = Utilities
        fields = ['option','id',]


class OutDoor_Spaces_Serializer (serializers.ModelSerializer):

    class Meta:
        model = OutDoor_Spaces
        fields = ['option','id',]


class Other_Amenities_Serializer (serializers.ModelSerializer):

    class Meta:
        model = Other_Amenities
        fields = ['option','id',]



class Appliances_Serializer (serializers.ModelSerializer):

    class Meta:
        model = Appliances
        fields = ['option','id',]



class Property_Serializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Properties
        fields = ['address_1','address_2','country','state','city','post_code','amount','number_of_unit',  'property_type','unit_number','number_of_storeys','number_of_bedroom_and_bathroon','parking_type','funished','utilities','outdoor_sapce', 'appliances','other_amenities','properties_image','properties_video','neighborhood_features','floor_area','ac_type',]



class List_Property_Serializer(serializers.ModelSerializer):
    # this is the get serializer
    property_type = Property_Type_Serializer( read_only = True , many = True )
    parking_type = Parking_Type_Serializer( read_only = True , many = True )
    utilities = Utilities_Serializer( read_only = True , many = True )
    outdoor_sapce = OutDoor_Spaces_Serializer( read_only = True , many = True )
    other_amenities = Other_Amenities_Serializer(  read_only = True , many = True )
    appliances = Appliances_Serializer ( read_only = True , many = True )


    class Meta: 
        model = Properties
        fields = ['id','address_1','address_2','country','state','city','post_code','amount','number_of_unit',  'property_type','unit_number','number_of_storeys','number_of_bedroom_and_bathroon','parking_type','funished','utilities','outdoor_sapce','appliances','other_amenities','properties_image','properties_video','neighborhood_features','floor_area','ac_type',]





