from django.urls import path
from . import views 

urlpatterns = [
    path('all-message/', views.Send_Message_View.as_view() , name = 'all-message'),
]


