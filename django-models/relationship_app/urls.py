from django.urls import path
from .views import list_books, LibraryDetailView
from . import views

urlpatterns = [
    path('library_detail/', views.LibraryDetailView, name='library'),
    path('list_books', views.list_books, name='books'),
]