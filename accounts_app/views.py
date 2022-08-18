from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from . import forms


# Create your views here.
from accounts_app.models import Account


def userlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home')
    return render(request, 'accounts_app/login.html')


def usersignup(request):
    if request.user.is_authenticated:
        return redirect('home:home')

    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        Account.objects.create_user(email=email, password=password)
        userlogin(request)
    return render(request, 'accounts_app/signup.html')



def userlogout(request):
    logout(request)
    return redirect('home:home')
