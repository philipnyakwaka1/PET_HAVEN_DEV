from django.urls import path
from . import views

urlpatterns = [
    path('index.html', views.index, name='index-view'),
    path('about.html', views.about, name='about-view'),
    path('login.html', views.login, name='login-view'),
    path('team.html', views.team, name='team-view'),
    path('testimonial.html', views.testimonial, name='testimonial-view'),
    path('blog.html', views.blog, name='blog-view'),
    path('detail.html', views.detail, name='detail-view'),
    path('shop.html', views.shop, name='shop-view'),
    path('404.html', views.page_not_found, name='404-view'),
    path('seller.html', views.seller, name='seller-view'),
]
