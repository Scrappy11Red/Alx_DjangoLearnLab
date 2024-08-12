from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.ChairField(max_length=200)
    author = models.ChairField(max_length=100)
    publication_year = models.IntegerField()
