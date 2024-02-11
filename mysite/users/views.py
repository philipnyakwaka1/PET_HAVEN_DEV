from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
from django.http import Http404


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
            if 'profile_update' in request.POST.keys():
                user = User.objects.get(pk=request.user.id)
                for key, val in request.POST.items():
                        if key not in ['csrfmiddlewaretoken', 'profile_update']:
                            if hasattr(user.profile, key):
                                setattr(user.profile, key, val)
                            else:
                                raise Http404(
                                    f'Attribute {key} does not exist in users profile')
                user.profile.save()
    return render(request, 'users/profile.html', {'instance': request.user.profile})
