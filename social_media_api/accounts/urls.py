from django.urls import path 
from .views import LoginView, LogoutView, RegisterView

urlpatterns = [
    path("register/", RegisterView, name=RegisterView),
    path("login/", LoginView, name=LoginView),
]
