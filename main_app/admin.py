from django.contrib import admin
from .models import Profile, City, Review, Photo

# Register your models here.
admin.site.register(Profile)
admin.site.register(City)
admin.site.register(Review)
admin.site.register(Photo)