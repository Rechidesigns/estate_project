from  . import views
from django.urls import path

urlpatterns = [
    path('send-otp/', views.OTP_View.as_view(), name='sendp-otp'),
    path('verify-otp/<str:email>/<int:otp_pin>/', views.OTP_Verification_View.as_view(), name='verify-otp'),
]
