from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='blog-index'),
               path('id/', views.blog, name='blog-id'),]
