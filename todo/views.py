from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todolist
from django.utils import timezone

def home(request):
    return render(request, 'todo/home.html')

def sign_up(request):
    if request.method == 'GET':
        return render(request, 'todo/sign_up.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password= request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/sign_up.html', {'form': UserCreationForm(), 'error':'This name already exists'})

        else:
            return render(request, 'todo/sign_up.html', {'form': UserCreationForm(), 'error':'The passwords did not match'})

def currenttodos(request):
    todos = Todolist.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'todo/currenttodos.html', {'todos':todos})

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/login.html', {'form': AuthenticationForm(), 'error':'Username or password did not match'})
        else:
            login (request, user)
            return redirect('currenttodos')


def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form':TodoForm()})
    else:
        form = TodoForm(request.POST)
        newtodo = form.save(commit=False)
        newtodo.user = request.user
        newtodo.save()
        return redirect('currenttodos')

def viewtodo(request, todo_pk):
        todo = get_object_or_404(Todolist, pk=todo_pk)
        if request.method == 'GET':
            form = TodoForm(instance=todo)
            return render(request, 'todo/detailtodo.html', {'todo':todo, 'form':form})
        else:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos')

def completetodo(request, todo_pk):
    todo = get_object_or_404(Todolist, pk=todo_pk, user = request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('detailtodos')
