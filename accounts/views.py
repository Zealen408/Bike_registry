from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import *

# Create your views here.

def register_request(request):
    if request.method == 'POST':
        form = userCrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'New user created.')
            return redirect('main:home')
        else:
            messages.error(request, 'Failed to create new user.')
            # return render(request, 'main/Register.html', {'form': form})
    form = userCrationForm()
    return render(request, 'accounts/Register.html', {'form': form})

def login_request(request):
    next = ''
    if request.GET:
        next = request.GET['next']



    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.first_name}.')
                if next != '':
                    return redirect(next)
                return redirect('main:home')


        else:
            messages.error(request, 'Invalid username or password')

    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_request(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return HttpResponseRedirect(reverse('main:home'))

@login_required()
def user_update_request(request):
    #user is active but not staff
    if request.method == 'POST':
        form = userProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your profile has been updated. Thank you.')
            return redirect('main:home')
        else:
            messages.error(request, 'Failed to save update, please correct the form.')
    form = userProfileForm(instance=request.user)
    return render(request, 'accounts/user_profile.html', {'form': form})
