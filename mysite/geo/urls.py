from django.urls import path
from . import views

urlpatterns = [path('states/<int:state_id>', views.state, name='state-id'),]
