from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('profile/', views.profile, name='profile'),
  path('accounts/signup/', views.signup, name='signup'),
  path('profile_setup/', views.profile_setup, name='profile_setup'),
  path('reviews/<int:review_id>/', views.reviews_detail, name='detail'),
]