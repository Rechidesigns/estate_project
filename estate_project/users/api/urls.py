from django.urls import path,include
from . import views

urlpatterns = [

    path('create-account/', views.Register_Account.as_view() , name = 'create_account'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('password_reset/', include('django_rest_passwordreset.urls')),
]
