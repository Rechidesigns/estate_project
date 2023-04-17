from django.urls import path
from . import views 

urlpatterns = [
    path('KYC-Application-Form/', views.Kyc_View.as_view(), name='KYC_Application'),
    path('KYC/<str:kyc_id>/', views.Kyc_Detail_View.as_view(), name='KYC_detail'),
]
