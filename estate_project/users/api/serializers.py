from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from estate_project.users.models import User
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin



User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class Account_Creation ( FriendlyErrorMessagesMixin , serializers.ModelSerializer ):
    ACCOUNT_TYPE = (
        ('Landlord', _('Landlord')),
        ('Tenant', _('Tenant')),
    )

    password = serializers.CharField(write_only=True)

    email = serializers.EmailField(
        help_text=_("The primary email address of the user."))

    contact_number = serializers.CharField(
        min_length=1,
        max_length=50,
        help_text=_('The contact number of the user.'))

    account_type = serializers.ChoiceField( choices = ACCOUNT_TYPE )

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name','email', 'contact_number', 'account_type' ]

    def get_cleaned_data(self):
        return {
                'name': self.validated_data.get('first_name') + " " + self.validated_data.get('last_name'),
                'first_name': self.validated_data.get('first_name'),
                'last_name': self.validated_data.get('last_name'),
                'email': self.validated_data.get('email'),
                'contact_number': self.validated_data.get('contact_number'),
                'account_type': self.validated_data.get('account_type'),
        }


    def validate_email(self, value):
        user_exist= User.objects.filter(email=value).exists()
        if user_exist:
            self.register_error(
                error_message=_('This email address used is already taken. Please login!'),
                error_code='email_taken',
                field_name='email')
        return value


    def validate_contact_number(self, value):
        contact_number= User.objects.filter(contact_number=value).exists()
        if contact_number:
            self.register_error(
                error_message=_('The contact number already exist.'),
                error_code='contact_number_exist',
                field_name='contact_number')
        return value


    def save(self, request):
        cleaned_data = self.get_cleaned_data()
        user = User(**cleaned_data)
        user.set_password(cleaned_data["password"])
        user.save()



    

    


    

    