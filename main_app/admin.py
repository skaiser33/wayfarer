from django.contrib import admin
from .models import Profile, City, Review

# Register your models here.
admin.site.register(Profile)
admin.site.register(City)
admin.site.register(Review)