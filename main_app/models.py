from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    current_city = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)