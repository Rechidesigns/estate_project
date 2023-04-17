from django.urls import path
from . import views 
from properties.api import views

urlpatterns = [
    path('property-type-options/', views.Property_Options_ViewSet.as_view() , name = 'property_type_options'),
    path('landlord-properties/' , views.Properties_View.as_view() , name = "properties_view"),
    path('property/<str:id>/', views.Property_Detail_View.as_view(), name='property-detail'),
    path('available-properties/' , views.Properties_List.as_view(), name = 'available_properties'),
]

