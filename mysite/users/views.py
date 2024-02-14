from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
from django.http import Http404
from .models import Pet, Order
from django.contrib.auth import logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}. Login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def home_page(request):
    return render(request, 'users/home.html')


@login_required
def profile(request):
    all_pets = Pet.objects.filter(owner=User.objects.get(pk=request.user.pk))
    if not all_pets.exists():
         all_pets = None
    return render(request, 'users/profile.html', {'pets': all_pets, 'user': request.user})

@login_required
def update_profile(request):
    if request.method == 'POST':
            if 'profile_update' in request.POST.keys():
                user = User.objects.get(pk=request.user.pk)
                for key, val in request.POST.items():
                        if key not in ['csrfmiddlewaretoken', 'profile_update']:
                            if 'profile_pic' in request.FILES:
                                user.profile.profile_pic = request.FILES['profile_pic']
                            if hasattr(user.profile, key):
                                setattr(user.profile, key, val)
                            else:
                                raise Http404(
                                    f'Attribute {key} does not exist in users profile')
                user.profile.save()
                return redirect('profile-view')
    return render(request, 'users/profile_information.html', {'user': request.user})

@login_required
def sell(request):
    return render(request, 'users/sell.html', {'user': request.user})

@login_required
def list_pet(request):
    if request.method == 'POST':
            if 'sell_pet' in request.POST.keys():
                pet_dict = dict(request.POST.items())
                del pet_dict['csrfmiddlewaretoken']
                del pet_dict['sell_pet']
                pet_dict['owner'] = User.objects.get(pk=request.user.pk)
                if 'image' in request.FILES:
                     pet_dict['image'] = request.FILES['image']
                listed_pet = Pet.objects.create(**pet_dict)
                return render(request, 'users/listed_pet.html', {'pet': listed_pet})
    return render(request, 'users/pet_information.html', {'user': request.user})

def logout_user(request):
     logout(request)
     messages.success(request, f'You have been logged out')
     return redirect('home-view')

"""
def login_user(request):
     if request.method == "POST":
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(request, username=username, password=password)
          if user:
               messages.success(request, f'You have been Logged In! Welcome to Pet Haven:')
               return redirect('home-view')
          else:
               messages.error(request, f'There was an error logging you in. Please try again ...')
               return redirect('login')
     else:
        return render(request, 'users/login.html')
"""