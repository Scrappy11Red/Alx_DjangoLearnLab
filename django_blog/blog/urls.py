from django.urls import path, include
from .views import register, update_user_profile

urlpatterns = [
    path("register/", register, name=register),
    path("update/", update_user_profile, name=update_user_profile),
]