from django.urls import path, include
from .views import register, update_user_profile, login, profile

urlpatterns = [
    path("register/", register, name=register),
    path("update/", update_user_profile, name=update_user_profile),
    path("login/", login, name=login)
    path("profile/", profile, name=profile)
]