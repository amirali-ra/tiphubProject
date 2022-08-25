from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('about-us', views.aboutus, name='aboutus'),
    path('', views.home, name='home')
]