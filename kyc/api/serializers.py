from rest_framework import serializers
from kyc.models import Kyc
# from estate_project.users.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Kyc_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Kyc
        exclude = ['id','created_date','modified_date', 'status', 'user_detail']
