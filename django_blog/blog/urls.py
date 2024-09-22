from django.urls import path
from .views import register,  login, profile, PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView, CommentCreateView, CommentDeleteView, CommentUpdateView

urlpatterns = [
    path("register/", register, name=register),
    path("login/", login, name=login),
    path("profile/", profile, name=profile),
    path("", PostListView, name=PostListView),
    path("post_list/<int:pk>/", PostDetailView, name=PostDetailView),
    path("post/<int:pk>/update/", PostUpdateView, name=PostUpdateView),
    path("post/<int:pk>/delete/", PostDeleteView, name=PostDeleteView),
    path("post/new/", PostCreateView, name=PostCreateView),
    path("post/<int:pk>/comments/new/", CommentCreateView, name=CommentCreateView),
    path("comment/<int:pk>/delete/", CommentDeleteView, name=CommentDeleteView),
    path("comment/<int:pk>/update/", CommentUpdateView, name=CommentUpdateView),
]