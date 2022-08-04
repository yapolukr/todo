from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('sign_up', views.sign_up, name='sign_up'),
    path('current', views.currenttodos, name='currenttodos'),
    path('logout', views.logoutuser, name='logoutuser'),
    path('create', views.createtodo, name='createtodo'),
    path('login', views.loginuser, name= 'loginuser'),

    path('', views.home, name='home'),
    path('current', views.currenttodos, name='currenttodos'),
    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),
    path('completed', views.completedtodos, name='completedtodos')
    ]