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

def eventsSearch(request):
    context = {
        'events': Event.objects.all(),
        }
    return render(request, "main/events_search.html", context)

def eventsInfo(request, id):
    currentEvent = get_object_or_404(Event, id=id)
    context = {
        'events': Event.objects.all(),
        'currentEvent': currentEvent,
    }
    return render(request, "main/events_info.html", context)

def eventsAdd(request):
    event = get_object_or_404(Event)
    userCurrent = request.user

    if request.method == 'POST':
        event.author = userCurrent.username
        event.startDate = 
        event.endDate =
        event.title = request.POST.get('title')
        event.description = request.POST.get('description')

        return redirect('events-search')

    return render(request, "main/events_add.html")

def calendar(request):
    context = {
        'events' : Event.objects.all()
    }
    return render(request, "main/calendar.html", context)

