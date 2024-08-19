from django.urls import path
from .views import list_books, LibraryDetailView, LoginView, LogoutView, register
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('library_detail/', views.LibraryDetailView, name='library'),
    path('list_books', views.list_books, name='books'),

    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html",
    next_page="home"), name="login"),
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html",
    next_page="home"), name="logout"),

    path("admin/", admin_view, name="Admin"),
    path("librarian/", librarian_view, name="Librarian"),
    path("member/", member_view, name="Member"),
]