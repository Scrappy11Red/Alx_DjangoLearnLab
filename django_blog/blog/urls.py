from django.urls import path, include
from .views import register, update_user_profile, login, profile, PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView

urlpatterns = [
    path("register/", register, name=register),
    path("update/", update_user_profile, name=update_user_profile),
    path("login/", login, name=login),
    path("profile/", profile, name=profile),
    path("", PostListView, name=PostListView),
    path("post_list/<int:pk>/", PostDetailView, name=PostDetailView),
    path("post/<int:pk>/update/", PostUpdateView, name=PostUpdateView),
    path("post/<int:pk>/delete/", PostDeleteView, name=PostDeleteView),
    path("post/new/", PostCreateView, name=PostCreateView),
]