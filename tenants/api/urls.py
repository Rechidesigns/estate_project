from django.urls import path
from . import views 

urlpatterns = [

    path('my-properties/', views.All_Free_Property_View.as_view() , name = 'all-tenants'),
    path('rent-properties/<str:property_id>/', views.Rent_Property_View.as_view() , name = 'rent-property'),
    # path('applicant-information/', views.Applicant_Information_Views.as_view() , name = 'Applicant-Informations'),
]


