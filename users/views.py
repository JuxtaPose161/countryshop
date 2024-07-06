from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from mainshop.models import Cart

from .form import UserRegisterForm, UserLoginForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Cart.objects.create(owner=new_user)
            login(request, new_user)
            return redirect('shop')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username = data['username'], password = data['password'])
            if user:
                login(request, user)
                return redirect('shop')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})
def logout_user(request):
    logout(request)
    return redirect('shop')
