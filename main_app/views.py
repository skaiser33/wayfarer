from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# from .forms import RegisterForm
from .forms import ProfileForm, ReviewForm
from .models import Profile, Review, City

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
  return render(request, 'profile/main.html', {'profile':profile, 'reviews':reviews})

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
@login_required
def profiles_edit(request, profile_id):
  profile = Profile.objects.get(id=profile_id)
  profile_form = ProfileForm(request.POST or None, instance=profile)
  if request.POST and profile_form.is_valid():
    profile_form.save()
    return redirect('profile')
  else:
    return render(request, 'profile/edit.html', { 'profile': profile, 'profile_form': profile_form })

# Define the reviews index view
# @login_required
def reviews_index(request):
  profile = Profile.objects.get(user=request.user)
  reviews = Review.objects.filter(profile_id=profile.id)
  return render(request, 'reviews/user_reviews/index.html', { 'reviews': reviews})    

# Define the reviews detail view
# @login_required
def reviews_detail(request, review_id):
  review = Review.objects.get(id=review_id)
  profile = Profile.objects.get(id=review.profile_id)
  return render(request, 'reviews/user_reviews/detail.html', {'review':review, 'profile':profile })

# Define the new review view
def reviews_new(request, city_id):
  review_form = ReviewForm(request.POST or None)
  profile = Profile.objects.get(user_id=request.user)
  if request.POST and review_form.is_valid():
    new_review = review_form.save(commit=False)
    new_review.city_id = city_id
    new_review.profile_id = profile.id
    new_review.save()
    return redirect('cities_detail', city_id=city_id)
  else:
    return render(request, 'reviews/new.html', {'review_form':review_form, 'city_id':city_id})

# Define the edit review view
# @login_required
def reviews_edit(request, review_id):
  review = Review.objects.get(id=review_id)
  review_form = ReviewForm(request.POST or None, instance=review)
  if request.POST and review_form.is_valid():
    review_form.save()
    return redirect('detail', review_id=review_id)
  else:
    return render(request, 'reviews/edit.html', { 'review': review, 'review_form': review_form })   

# Define the delete review view
# @login_required
def reviews_delete(request, review_id):
  Review.objects.get(id=review_id).delete()
  return redirect('index')         

#Define the cities index view
def cities_index(request):
  cities = City.objects.all()
  return render(request, 'cities/index.html', {'cities':cities })

# Define the city details view
def cities_detail(request, city_id):
  city = City.objects.get(id=city_id)
  reviews = Review.objects.filter(city_id=city_id)
  return render(request, 'cities/detail.html', {'reviews':reviews, 'city':city})

# STYLING TEST ONLY for cities pageDefine the about view
def cities_test(request):
  return render(request, 'cities_test.html')
  return render(request, 'reviews/user_reviews/detail.html', {'review':review, 'profile':profile })
