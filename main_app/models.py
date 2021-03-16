from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms

# Create your models here.
class Profile(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  current_city = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  