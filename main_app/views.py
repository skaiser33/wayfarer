from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# from .forms import RegisterForm
from .forms import ProfileForm
from .models import Profile

# Define the home view
def home(request):
  return render(request, 'home.html')

# Define the about view
def about(request):
  return render(request, 'about.html')

# Define the profile view
def profile(request):
  return render(request, 'profile.html')

# def signup(request):
#   error_message = ''
#   if request.method == 'POST':
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#       user = form.save()
#       login(request, user)
#       return redirect('profile_setup.html')
#     else:
#       error_message = 'Invalid sign up - try again'
#   form = UserCreationForm()
#   context = {'form': form, 'error_message': error_message }
#   return render(request, 'registration/signup.html', context)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('profile_setup')
    else:
      print(form.errors.as_json())
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
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

# # profile setup form
# def profile_setup(request):
#   # return render(request, 'profile_setup.html')
#   error_message = ''
#   if request.method == 'POST':
#     form = ProfileForm(request.POST)
#     if form.is_valid():
#       profile = form.save(commit=False)
#       profile.user_id = request.user.id
#       profile = form.save()
#       return redirect(request, 'profile')
#     else:
#       error_message = 'Invalid sign up - try again'
#   form = ProfileForm()
#   context = {'form': form, 'error_message': error_message }
#   return render(request, 'profile_setup.html', context)



# wayfarer
