from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100, blank=True)
    college = models.CharField(max_length=150, blank=True)
    degree = models.CharField(max_length=100, blank=True)
    branch = models.CharField(max_length=100, blank=True)
    graduation_year = models.PositiveIntegerField(null=True, blank=True)
    skills = models.TextField(blank=True)
    career_goal = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.user.username