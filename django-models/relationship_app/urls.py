from django.urls import path
from .views import book_list, LibraryDetailView
from . import views

urlpatterns = [
    path('library_detail/', views.LibraryDetailView, name='library'),
    path('list_books', views.books_list, name='books'),
]