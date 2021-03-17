from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
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
    user = request.user
    print(request.user.id)
    login(request, user)
    new_profile = profile_form.save(commit=False)
    new_profile.user = request.user
    new_profile.save()  
    return redirect('profile')
  else:
    return render(request, 'profile_setup.html', { 'profile_form': profile_form })

# Define the view to edit profile
def profiles_edit(request, profile_id):
  profile = Profile.objects.get(id=profile_id)
  profile_form = ProfileForm(request.POST or None, instance=profile)
  if request.POST and profile_form.is_valid():
    profile_form.save()
    return redirect('detail', profile_id=profile_id)
  else:
    return render(request, 'profile/edit.html', { 'profile': profile, 'profile_form': profile_form })

# Define the reviews index view
def reviews_index(request):
  profile = Profile.objects.get(user=request.user)
  reviews = Review.objects.filter(profile_id=profile.id)
  return render(request, 'user_reviews/index.html', { 'reviews': reviews})    

# Define the reviews detail view
def reviews_detail(request, review_id):
  review = Review.objects.get(id=review_id)
  profile = Profile.objects.get(id=review.profile_id)
  return render(request, 'user_reviews/detail.html', {'review':review, 'profile':profile })