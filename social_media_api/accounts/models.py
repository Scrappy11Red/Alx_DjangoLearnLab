from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    username = models.CharField(max_length=25)
    handle = models.CharField(max_length=25)
    bio = models.CharField(max_length=105)
    header = models.ImageField()
    profile_picture = models.ImageField()
    followers = models.ManyToManyField("self", symmetrical=False, related_name="followers")
    following = models.ManyToManyField("self", symmetrical=False, related_name="following")
    date_joined = models.DateTimeField()