from django.urls import path
from . import views 

urlpatterns = [
    path('all-Tenants/<str:property_id>/', views.Rent_Property_View.as_view() , name = 'all-tenants'),
]


