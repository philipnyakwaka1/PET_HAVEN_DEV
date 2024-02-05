from django.urls import path
from . import views

urlpatterns = [path('users', views.get_users, name='profiles-view'),
               path('users/<int:id>', views.get_user_by_id, name='user-profile')]
