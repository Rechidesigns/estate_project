from django.urls import path
from . import views

urlpatterns = [

    path('create-account/', views.Register_Account.as_view() , name = 'create_account'),
    # path('add-kyc/', views.KYC_View.as_view(), name = 'add_kyc'),

]