from django.urls import path
from . import views 
from properties.api import views

urlpatterns = [
    path('property-type-options/', views.Property_Options_ViewSet.as_view() , name = 'property_type_options'),
    path('landlord-properties/' , views.Properties_View.as_view() , name = "properties_view"),
    path('property/<str:p_id>/', views.Property_Detail_View.as_view(), name='property-detail'),
    path('comments/' , views.Comment_View.as_view() , name = "comments_view"),

]

