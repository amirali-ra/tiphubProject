from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login', views.userlogin, name='login'),
    path('logout', views.userlogout, name='logout'),
    path('signup', views.usersignup, name='signup')
]