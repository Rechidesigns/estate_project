from rest_framework import serializers

from tenants.models import Tenant






class Tenant_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Tenant
        fields = ['id', 'user', 'properties']