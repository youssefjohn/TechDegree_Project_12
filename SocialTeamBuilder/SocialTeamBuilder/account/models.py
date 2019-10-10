from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserSkills(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class User_details(models.Model):
    relation = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    picture = models.ImageField(upload_to='profile_pictures', blank=True)
    skills = models.ManyToManyField(UserSkills, blank=True)


class PositionModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    related_skill = models.ManyToManyField(UserSkills, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=None)
    position = models.ManyToManyField(PositionModel, blank=True, default=None)
    project_timeline = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title




















