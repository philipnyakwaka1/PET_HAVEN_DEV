from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username} details {request.POST} cleaned_data {form.cleaned_data}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def home_page(request):
    return render(request, 'users/home.html')


@login_required
def profile(request):
    if request.method == 'POST':

        user = User.objects.get(username=request.user)
        user.profile.first_name = request.POST['first_name']
        user.profile.last_name = request.POST['last_name']
        user.profile.profile_pic = request.POST['profile_pic']
        user.profile.address = request.POST['address']
        user.profile.phone = request.POST['phone']
        user.profile.save()
    return render(request, 'users/profile.html', {'instance': request.user})
