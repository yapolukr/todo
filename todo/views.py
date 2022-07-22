from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def sign_up(request):
    if request.method == 'GET':
        return render(request, 'todo/sign_up.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password= request.POST['password1'])
                user.save()
                return render(request, 'todo/cabinet.html')
            except IntegrityError:
                return render(request, 'todo/sign_up.html', {'form': UserCreationForm(), 'error':'This name already exists'})

        else:
            return render(request, 'todo/sign_up.html', {'form': UserCreationForm(), 'error':'The passwords did not match'})

