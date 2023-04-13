from django.urls import path
from . import views
# from knox.views import LogoutView, LogoutAllView


# urlpatterns = [
#     path('login/', views.LoginAPIView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('logout-all/', LogoutAllView.as_view(), name='logout-all'),
# ]


from django.urls import path
from .views import LoginView, LogoutView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
