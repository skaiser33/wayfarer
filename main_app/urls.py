from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('profile/', views.profile, name='profile'),
  path('accounts/signup/', views.signup, name='signup'),
  path('profile_setup/', views.profile_setup, name='profile_setup'),
  path('profile/<int:profile_id>/edit/', views.profiles_edit, name="edit_profile"),
  path('profile/<int:profile_id>/add_photo/', views.add_photo, name='add_photo'),
  path('reviews/', views.reviews_index, name='index'),
  path('reviews/new/cities/<int:city_id>/', views.reviews_new, name='new_review'),
  path('reviews/<int:review_id>/edit/', views.reviews_edit, name="edit"),
  path('reviews/<int:review_id>/delete/', views.reviews_delete, name="delete"),
  path('reviews/<int:review_id>/', views.reviews_detail, name='detail'),
  path('cities/', views.cities_index, name='cities_index'),
  path('cities/?', views.cities_search, name='cities_search'),
  path('cities/<int:city_id>/', views.cities_detail, name='cities_detail'),
  path('cities_test/', views.cities_test, name='cities_test'),
]