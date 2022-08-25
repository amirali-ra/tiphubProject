from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.activate,
         name='activate'),
    path('login', views.userlogin, name='login'),
    path('logout', views.userlogout, name='logout'),
    path('signup', views.usersignup, name='signup')
]