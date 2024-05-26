from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import  messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.firstName = form.cleaned_data.get('firstName')
            user.lastName = form.cleaned_data.get('lastName')
            username = form.cleaned_data.get('username')

            messages.success(request, f'Konto {username} utworzone')
            return redirect('events-search')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})