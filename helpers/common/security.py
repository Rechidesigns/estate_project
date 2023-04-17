from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException


from secrets import compare_digest
from django.conf import settings

from recuity.users.models import User


class SignatureMissMatch(APIException):
    """Raised when the signatures are not matched."""
    status_code = 401
    default_detail = "Signature header is invalid."
    default_code = "signature_invalid"


class SignatureHeaderMissing(APIException):
    """Raised when the request does not have the signature."""
    status_code = 401
    default_detail = "Signature header is missing. Make sure Recuity-Authentication-Token is present in header. contact the developer rechi@gmail.com"
    default_code = "signature_header_missing"


class APIAccessDenied(APIException):
    status_code = 401
    default_detail = "API Access Denied. Signature is not valid. contact the developer rechi@gmail.com"
    default_code = "api_access_denied"


class MerchantAccessDenied(APIException):
    status_code = 404
    default_detail = "Your account is not permitted to take any of this actions, if you are having issues with your account , you can also contact your administrator . Still facing an issues email developer@rechi.com"
    default_code = "merchant_access_denied"


class RecuityPermission(BasePermission):

    def has_permission(self, request, *args, **kwargs):
        # Checking if the KOK auth is been authorized
        # is been authorized by switching it to true
       
        given_token = request.headers.get("Recuity-Authentication-Token", None)
        if settings.RECUITY_AUTH:
            if not given_token:
                raise SignatureHeaderMissing()
            return given_token == settings.RECUITY_AUTH_KEYS
        
        else:
            given_token = None
            return given_token == None



class RecuityMerchantPermission (BasePermission):

    def has_permission(self, request, *args, **kwargs):
        # this hold the permission for user account
        # to verify if the user is a merchant user or not
        email = request.user.email # the merchant email address
        try:
            user_account_type = User.objects.get ( email = email , is_active = True , account_type = "Landlord" )
        except User.DoesNotExist:
            raise MerchantAccessDenied()
        return user_account_type
    


class RecuityTenantPermission (BasePermission):

    def has_permission(self, request, *args, **kwargs):
        # this hold the permission for user account
        # to verify if the user is a Tenant user or not
        email = request.user.email # the Tenant email address
        try:
            user_account_type = User.objects.get ( email = email , is_active = True , account_type = "Tenant" )
        except User.DoesNotExist:
            raise MerchantAccessDenied()
        return user_account_type







