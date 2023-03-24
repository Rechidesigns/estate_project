from django.urls import path
from . import views

urlpatterns = [

    path('create-account/', views.Register_Account.as_view() , name = 'create_account'),
    # path('add-kyc/', views.Applicant_Information_KYC_View.as_view(), name = 'add_kyc'),
    # path('kyc/<str:kyc_id>', views.Applicant_Information_Detail_View.as_view(), name = 'kyc'),
]
