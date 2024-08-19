from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    role_choices = (
        ("ADMIN", "Admin"),
        ("LIBRARIAN", "Librarian"),
        ("MEMEBER", "Member"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=role_choices)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
 
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)