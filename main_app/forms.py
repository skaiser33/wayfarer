from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
  first_name = forms.CharField(max_length=100, help_text='first_name')
  last_name = forms.CharField(max_length=100, help_text='last_name')
  current_city = forms.CharField(max_length=100, help_text='current_city')
  
  class Meta:
    model = User
    fields = ["username", "password1", "password2", "first_name", "last_name", "email", "current_city"]