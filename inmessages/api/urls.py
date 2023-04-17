from django.urls import path
from . import views 

urlpatterns = [
    path('all-message/', views.All_messages_View.as_view() , name = 'all-message'),
    path('messages/', views.Send_Message_View.as_view(), name='send_message'),

]

