from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-view'),
    path('profile', views.profile, name='profile-view'), 
    path('sell', views.sell, name="sell-pet"),
    path('list_pet', views.list_pet, name="list-pet"),
    path('update_profile', views.update_profile, name="profile-update"),
    #path('login', views.login_user, name='login'),
    path('logout/', views.logout_user, name="logout"),
    ]
