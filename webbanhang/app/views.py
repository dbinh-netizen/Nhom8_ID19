from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'app/home.html')

def player_register(request):
    return render(request, 'app/player_register.html')

def dev_register(request):
    return render(request, 'app/dev_register.html')

def des_register(request):
    return render(request, 'app/des_register.html')

def dev_login(request):
    return render(request, 'app/dev_login.html')

def des_login(request):
    return render(request, 'app/des_login.html')
