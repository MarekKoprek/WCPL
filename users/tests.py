from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render

from .forms import UserRegisterForm

@transaction.atomic
def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            try:
                # Operacje bazodanowe
                user = form.save()
                # Inne operacje bazodanowe
                # ...

                # Zatwierdzenie transakcji
                transaction.commit()
                return HttpResponse("User registered successfully!")
            except Exception as e:
                # W przypadku błędu, wycofanie transakcji
                transaction.rollback()
                return HttpResponse("Error occurred while registering user: {}".format(str(e)))
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
