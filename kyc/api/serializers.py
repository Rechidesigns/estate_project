from rest_framework import serializers
from kyc.models import Kyc
# from estate_project.users.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Kyc_Serializer(serializers.ModelSerializer):
   
    class Meta:
        model = Kyc
        fields = ['legal_first_name', 'legal_last_name', 'address_line_1', 'address_line_2',
                  'state', 'zip_code', 'city', 'phone_number_1', 'phone_number_2', 'proof_of_address_type',
                  'proof_of_address_file', 'gender', 'date_of_birth', 'profile_image', 'personal_references',
                  'rental_history', 'employment_income', 'credit_check', 'criminal_security_background_check',
                  'nationality', 'second_nationality', 'type_of_identification', 'photo_type_of_identification',
                  'created_date', 'status', 'country',
                  ]
