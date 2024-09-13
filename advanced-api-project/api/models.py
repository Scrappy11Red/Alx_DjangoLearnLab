from django.db import models

# Create your models here.

#Creates Author Model
class Author(models.Model):
    name = models.CharField(max_length=50)
    #Return Author name as a string
    def __str__(self):
        return self.name
    

#Creates Book Model
class Book(models.Model):
    title = models.CharField(max_length=25)
    publication_year = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    #Returns Book title as a string
    def __str__(self):
        return self.title

