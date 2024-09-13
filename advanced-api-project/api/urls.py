from .models import Book, Author
from django.urls import path
from . import views

ulrpatterns = [
    path('books/', views.BookLlistView.as_view(), name='book-list'),
    path('books/create/', views.BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', views.BookListDetailView.as_view(), name='book-detail'),
    path('books/update/', views.BookListUpdateView.as_view(), name='book-update'),
    path('books/delete/', views.BookListDeleteView.as_view(), name='book-delete'),
]