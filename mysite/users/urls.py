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
    path('shop', views.shop, name="shop-view"),
    path('order', views.order_pet, name='order-view'),
    #path('terms', views.terms_page, name="terms-view"),
    path('pet/<int:pet_id>', views.pet_profile, name="pet-profile"),
    path('about', views.about_page, name="about-view"),
    path('team', views.team_page, name="team-view"),
    path('blog', views.blog_page, name="blog-view"),
    path('testimonial', views.testimonial_page, name="testimonial-view"),
    ]
