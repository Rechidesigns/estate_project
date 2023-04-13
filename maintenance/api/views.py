from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from .serializers import Maintenance_Serializer
from maintenance.models import Maintenance
from django.http import Http404




# User = get_user_model()

# class MaintainanceRequestView(APIView):
#     permission_classes = (IsAuthenticated,)
#     def post(self, request):
#         if  not request.user.account_type == "landlord":
#             return Response({"error": "permission error"}, 404)
#         try:
#             user = User.objects.filter(account_type="landlord")

        










# class TenantMaintainanceRequest(APIView):
#     permission_classes = (IsAuthenticated,)


#     def post(self, request):
#         serializer = Maintenance_Serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(tenant=request.user)

#         return Response({"message": "successfuly made a maintainance request"}, status=200)





