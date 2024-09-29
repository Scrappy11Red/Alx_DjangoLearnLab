from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    content = models.TextField(max_length=250)
    create_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Comments(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    create_at = models.DateTimeField()
    updated_at = models.DateTimeField()




# Post should have fields like author (ForeignKey to User), title, content, created_at, and updated_at.
# Comment should reference both Post (ForeignKey) and User (author), with additional fields for content, created_at, and updated_at.