from rest_framework import serializers

from properties.models import Properties
from tenants.models import Tenant
from estate_project.users.models import User

class User_Info ( serializers.ModelSerializer ):

    class Meta:
        model = User
        fields = ('name', 'email',)



class Property_Details ( serializers.ModelSerializer ):

    class Meta:
        model = Properties
        fields = ('landlord', 'amount', 'number_of_unit','property_type','unit_number','number_of_storeys','number_of_bedroom_and_bathroon',)



class None_Rented_Properties (serializers.ModelSerializer):
    landlord = User_Info( read_only= True )
    properties = Property_Details( read_only= True )

    class Meta:
        model = Tenant
        fields = ['id','landlord', 'properties','notification','status', 'action_date', 'created_date']

        