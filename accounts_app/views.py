from django.shortcuts import render

# Create your views here.


def userlogin(request):
    return render(request, 'accounts_app/login.html')