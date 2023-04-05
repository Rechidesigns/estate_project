from django.urls import path
from . import views 
from comments.api import views

urlpatterns = [
    path('comments/' , views.Comment_View.as_view() , name = "comments_view"),
]

