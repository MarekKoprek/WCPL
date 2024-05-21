from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile


def profileHome(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    context = {
        'user' : user,
        'profile' : profile
    }

    return render(request, 'main/profile_home.html', context)

def eventsSearch(request):
    return render(request, "main/events_search.html")

def calendar(request):
    return render(request, "main/calendar.html")
