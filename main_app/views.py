from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# from .forms import RegisterForm
from .forms import ProfileForm
from .models import Profile, Review

# Define the home view
def home(request):
  return render(request, 'home.html')

# Define the about view
def about(request):
  return render(request, 'about.html')

# Define the profile view
def profile(request):
  profile = Profile.objects.get(user=request.user)
  reviews = Review.objects.filter(profile_id=profile.id)
  return render(request, 'profile.html', {'profile':profile, 'reviews':reviews})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('profile_setup')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message }
  return render(request, 'registration/signup.html', context)

def profile_setup(request):
  profile_form = ProfileForm(request.POST or None)
  if request.POST and profile_form.is_valid():
    new_profile = profile_form.save(commit=False)
    new_profile.user = request.user
    new_profile.save()
    return redirect('profile')
  else:
    return render(request, 'profile_setup.html', { 'profile_form': profile_form })

# wayfarer