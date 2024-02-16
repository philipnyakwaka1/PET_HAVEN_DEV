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
"""
def terms_page(request, pet_id):
     return render(request, 'users/terms.html', {'pet_id': pet_id})
"""


@login_required
def profile(request):
    all_pets = Pet.objects.filter(owner=User.objects.get(pk=request.user.pk))
    if not all_pets.exists():
         all_pets = None
    orders_as_customer = Order.objects.filter(customer=request.user)
    if not orders_as_customer.exists():
         orders_as_customer = None
    orders_as_seller = Order.objects.filter(seller=request.user)
    if not orders_as_seller.exists():
         orders_as_seller = None
    return render(request, 'users/profile.html', {'pets': all_pets, 'user': request.user, 'orders_as_customer': orders_as_customer, 'orders_as_seller': orders_as_seller})

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
            
            if 'unlist_pet' in request.POST.keys():
                  pet_id = request.POST.get('unlist_pet')
                  pet = Pet.objects.get(pk=pet_id)
                  pet.delete()
                  messages.success(request, f'You have succesfully unlisted {pet.name}')
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

def shop(request):
        all_pets = Pet.objects.all() 
        if request.method == 'POST':
             if 'pet_id' in request.POST.keys():
                  pet_id = request.POST.get('pet_id')
                  return render(request, 'users/terms.html', {'pet_id': pet_id})
             else:
                if 'search_btn_value' in request.POST.keys():
                    radio_value = request.POST.get('radio_value', '')
                    breed = request.POST.get('search_text', '').strip()
                    if len(breed) > 0:
                        if radio_value == 'dog':
                                all_pets = Pet.objects.filter(specie='dog', breed=breed)
                        elif radio_value == 'cat':
                                all_pets = Pet.objects.filter(specie='cat', breed=breed)
                        elif radio_value == 'bird':
                                all_pets = Pet.objects.filter(specie='bird', breed=breed)
                        elif radio_value == 'rabbit':
                                all_pets = Pet.objects.filter(specie='rabbit', breed=breed)
                        else:
                                all_pets = Pet.objects.filter(breed=breed)
                    else:
                        if request.POST['radio_value'] == 'dog':
                            all_pets = Pet.objects.filter(specie='dog')
                        elif request.POST['radio_value'] == 'cat':
                            all_pets = Pet.objects.filter(specie='cat')
                        elif request.POST['radio_value'] == 'bird':
                            all_pets = Pet.objects.filter(specie='bird')
                        elif request.POST['radio_value'] == 'rabbit':
                            all_pets = Pet.objects.filter(specie='rabbit')
                        else:
                                all_pets = Pet.objects.all()
                else:
                    all_pets = Pet.objects.all()
        if not all_pets.exists():
             all_pets = None      
        return render(request, 'users/shop.html', {'pets': all_pets})

def order_pet(request):
     if request.method == 'POST':
          pet_id = request.POST.get('pet_id')
          pet = Pet.objects.get(pk=pet_id)
          customer = User.objects.get(pk=request.user.pk)
          seller = User.objects.get(pk=pet.owner.pk)
          Order.objects.create(pet=pet, customer=customer, seller=seller)
          messages.success(request, f'You have succesfully listed your order. Kindly check your orders and contact the owner')
          return redirect('profile-view')
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