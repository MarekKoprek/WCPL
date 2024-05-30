from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Profile, Event
from json import dumps


def profileHome(request, username):
    userInfo = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=userInfo)
    userCurrent = request.user

    if request.method == 'POST':
        userInfo.first_name = request.POST.get('first_name', '')
        userInfo.last_name = request.POST.get('last_name', '')
        userInfo.email = request.POST.get('email', '')

        profile.phone_number = request.POST.get('phone_number', '')
        profile.faculty = request.POST.get('faculty', '')
        profile.course = request.POST.get('course', '')
        profile.semester = request.POST.get('semester', '')
        profile.bio = request.POST.get('bio', '')

        userInfo.save()
        profile.save()

        return redirect('profile-home', username=username)

    context = {
        'userInfo' : userInfo,
        'profile' : profile,
        'userCurrent' : userCurrent
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

participantRows = [1, 2]
participantColumns = [1, 2, 3, 4]

def eventsSearch(request):
    context = {
        'events': Event.objects.all(),
        'participantRows': participantRows,
        'participantColumns': participantColumns
        }
    return render(request, "main/events_search.html", context)

def eventsAdd(request):
    return render(request, "main/events_add.html")

def calendar(request):
    context = {
        'events' : Event.objects.all()
    }
    return render(request, "main/calendar.html", context)

