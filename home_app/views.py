from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home_app/index.html')


def aboutus(request):
    return render(request, 'home_app/about-us.html')
