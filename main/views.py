from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Profile, Event
from .forms import EventForm, ParticipationForm
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
    currentUser = request.user
    
    if request.method == 'POST':
        form = ParticipationForm(request.POST)
        currentEvent.users.add(currentUser)
        currentEvent.save()
    else:
        form = ParticipationForm()
        
    context = {
        'events': Event.objects.all(),
        'currentEvent': currentEvent,
        'form': form
    }
    return render(request, "main/events_info.html", context)

def eventsAdd(request):
    userCurrent = request.user
    
    if request.method == 'POST':
        form = EventForm(request.POST)
        author = userCurrent
        title = request.POST.get('title')
        description = request.POST.get('description')
        Event.objects.create(author=author, title=title, description=description)
        return redirect('events-search')
    else:
        form = EventForm()
    return render(request, "main/events_add.html", {'form': form})

def calendar(request):
    context = {
        'events' : Event.objects.all()
    }
    return render(request, "main/calendar.html", context)

