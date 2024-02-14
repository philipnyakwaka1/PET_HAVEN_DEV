from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-view'),
    path('profile', views.profile, name='profile-view'), 
    path('sell', views.sell, name="sell-pet"),
    path('list_pet', views.list_pet, name="list-pet")
    ]
