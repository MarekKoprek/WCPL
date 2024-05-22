from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile, Event


def profileHome(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    context = {
        'user' : user,
        'profile' : profile
    }

    return render(request, 'main/profile_home.html', context)

events_ = [
    {
        'title': 'Tytuł ogłoszenia',
        'description': 'Ogólny opis wydarzenia cokolwiek tutaj może być.',
        'date': '25.12.2023'
    },
    {
        'title': 'Tytuł ogłoszenia',
        'description': 'Ogólny opis wydarzenia cokolwiek tutaj może być.',
        'date': '26.12.2023'
    },
    {
        'title': 'Tytuł ogłoszenia',
        'description': 'Ogólny opis wydarzenia cokolwiek tutaj może być.',
        'date': '27.12.2023'
    },
    {
        'title': 'Tytuł ogłoszenia',
        'description': 'Ogólny opis wydarzenia cokolwiek tutaj może być.',
        'date': '28.12.2023'
    },
    {
        'title': 'Tytuł ogłoszenia',
        'description': 'Ogólny opis wydarzenia cokolwiek tutaj może być.',
        'date': '29.12.2023'
    },
    {
        'title': 'Tytuł ogłoszenia',
        'description': 'Ogólny opis wydarzenia cokolwiek tutaj może być.',
        'date': '30.12.2023'
    },
    {
        'title': 'Tytuł ogłoszenia',
        'description': 'Ogólny opis wydarzenia cokolwiek tutaj może być.',
        'date': '31.12.2023'
    }
]

participantRows = [1, 2, 3, 4]

def eventsSearch(request):
    context = {
        'events': Event.objects.all(),
        'participantRows': participantRows
        }
    return render(request, "main/events_search.html", context)

def eventsAdd(request):
    return render(request, "main/events_add.html")

def calendar(request):
    return render(request, "main/calendar.html")
