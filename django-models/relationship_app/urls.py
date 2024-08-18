from django.urls import path
from .views import list_books, LibraryDetailView
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('library_detail/', views.LibraryDetailView, name='library'),
    path('list_books', views.list_books, name='books'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html",
    next_page="home"), name="logout"),
]