from django.contrib import admin
from .models import Profile, Pet, Order

admin.site.register([Profile, Pet, Order])
