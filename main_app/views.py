from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from .models import Profile

# Define the home view
def home(request):
  return render(request, 'home.html')

# Define the about view
def about(request):
  return render(request, 'about.html')

# Define the profile view
def profile(request):
  profile = Profile.objects.get(user=request.user)
  return render(request, 'profile.html', {'profile':profile})


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return render(request, 'profile.html')
    else:
      error_message = 'Invalid sign up - try again'
  form = RegisterForm()
  context = {'form': form, 'error_message': error_message }
  return render(request, 'registration/signup.html', context)


