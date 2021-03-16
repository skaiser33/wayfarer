from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  current_city = models.CharField(max_length=100)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.first_name


class City(models.Model):
  name = models.CharField(max_length=100)
  image = models.CharField(max_length=200)
  profiles = models.ManyToManyField(Profile, through='Review')

  def __str__(self):
    return self.name

class Review(models.Model):
  title = models.CharField(max_length=200, blank=False)
  content = models.TextField(blank=False)
  date = models.DateField(auto_now_add=True)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  city = models.ForeignKey(City, on_delete=models.CASCADE)