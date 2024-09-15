from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author


class Book(APITestCase):
    def setUp(self):
        Book.objects.create(title='Harry Potter and the prisoner of Azkaban', publication_year=2000)
        Book.objects.create(title='Eat, Pray, Love', publication_year=2014)
