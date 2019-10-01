from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class User_details(models.Model):
    relation = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    picture = models.ImageField(upload_to='profile_pictures', blank=True)


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

























