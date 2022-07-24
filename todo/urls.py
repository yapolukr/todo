from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('sign_up', views.sign_up, name='sign_up'),
    path('current', views.currenttodos, name='currenttodos'),
    path('logout', views.logoutuser, name='logoutuser'),
    path('login', views.loginuser, name='loginuser'),

    path('', views.home, name='home'),

    ]