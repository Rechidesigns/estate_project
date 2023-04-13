from rest_framework import serializers
from maintenance.models import Maintenance

class Maintenance_Serializer(serializers.ModelSerializer):


    class Meta:
        model = Maintenance
        feilds = [ 
                  'tenant',
                  'maintenance_type',
                  'issue',
                  'action',
                  'status',
                  
                  ]