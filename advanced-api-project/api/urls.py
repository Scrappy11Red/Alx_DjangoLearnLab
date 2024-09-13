from .models import Book, Author
from django.urls import path
from .views import BookListCreateView, BookListDeleteView, BookListDetailView, BookListUpdateView
from .views import 

ulrpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookListDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookListUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookListDeleteView.as_view(), name='book-delete'),
]