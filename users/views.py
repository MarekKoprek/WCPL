from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib import  messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, f'Konto {username} utworzone')
            return redirect('events-search')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

def login(request):
    return render(request, 'users/login.html')

def logoutUser(request):
    if(request.user.username != None):
        logout(request)
    return redirect('login')
