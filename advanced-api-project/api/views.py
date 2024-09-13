from django.shortcuts import render
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework

# Create your views here.

#Creates a ListView for retrieving all books.
class BookListView(generics.ListView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #Applies Django REST Framework’s permission classes to protect API endpoint based on user roles.
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']

    def perform_create(self, serializer):
        serializer.save()

#Creates a DetailView for retrieving a single book by ID.
class BookListDetailView(generics.DetailView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #Applies Django REST Framework’s permission classes to protect API endpoint based on user roles.
    permission_classes = [IsAuthenticatedOrReadOnly]

#Creates a CreateView for adding a new book.
class BookListCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #Applies Django REST Framework’s permission classes to protect API endpoint based on user roles.
    permission_classes = [IsAuthenticated]

    def create_book(self, serializer):
        serializer.save(creator=self.request.user)

#Creates an UpdateView for modifying an existing book.
class BookListUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #Applies Django REST Framework’s permission classes to protect API endpoint based on user roles.
    permission_classes = [IsAuthenticated]

#Creates a DeleteView for removing a book.
class BookListDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #Applies Django REST Framework’s permission classes to protect API endpoint based on user roles.
    permission_classes = [IsAuthenticated]

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()