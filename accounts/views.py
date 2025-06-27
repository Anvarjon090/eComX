from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileUpdateForm


@login_required
def profile_update_view(request):
    if request.method == 'POST':
        bio = request.POST.get('bio')
        phone_number = request.POST.get('phone_number')

        # Misol uchun: user modeli yangilanmoqda
        request.user.bio = bio
        request.user.phone_number = phone_number
        request.user.save()

        return redirect('accounts:profile')

    return render(request, 'auth/profile_update.html')
def profile_view(request):
    return render(request, 'auth/profile.html')

def logout_view(request):
    logout(request)
    return redirect('common:index')     

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('common:index')
        else:
            return render(request, 'auth/login.html', {'error': 'Invalid credentials'})
    return render(request, 'auth/login.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Avtomatik login qilish
            return redirect('common:index')  # Ro‘yxatdan o‘tganidan so‘ng bosh sahifaga yo‘naltirish
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # kerakli sahifaga qayta yo'naltirish
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'auth/profile.html', {'form': form})