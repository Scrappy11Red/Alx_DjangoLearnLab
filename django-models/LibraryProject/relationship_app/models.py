from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField()
    books = models.ManyToManyField(Book, on_delete=models.CASCADE, related_name='Libraries')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField()
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarians')

    def __str__(self):
        return self.name
