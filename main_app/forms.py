from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Review

class ProfileForm(forms.ModelForm):
  first_name = forms.CharField(max_length=100)
  last_name = forms.CharField(max_length=100)
  current_city = forms.CharField(max_length=100)
  
  class Meta:
    model = Profile
    fields = ["first_name", "last_name", "current_city"]

class ReviewForm(forms.ModelForm):
  title = forms.CharField(max_length=200, required=True)
  content = forms.CharField(required=True, label="Content", widget=forms.Textarea())
  
  class Meta:
    model = Review
    fields = ["title", "content"]
