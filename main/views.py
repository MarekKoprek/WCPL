from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Profile, Event
from .forms import EventForm, ParticipationForm
from json import dumps
from datetime import datetime


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
        if currentUser.username != 'admin':
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
        startDate = request.POST.get('dateBegin')
        startDateList = startDate.split('-')
        startTime = request.POST.get('hourBegin')
        startTimeList = startTime.split(':')
        endDate = request.POST.get('dateEnd')
        endDateList = endDate.split('-')
        endTime = request.POST.get('hourEnd')
        endTimeList = endTime.split(':')
        
        startDate = datetime(int(startDateList[0]), int(startDateList[1]), int(startDateList[2]), int(startTimeList[0]), int(startTimeList[1], 0))
        endDate = datetime(int(endDateList[0]), int(endDateList[1]), int(endDateList[2]), int(endTimeList[0]), int(endTimeList[1], 0))
        
        if(startDate > endDate):
            return redirect('events-add')
            
        Event.objects.create(author=author, 
                            title=title, 
                            description=description, 
                            startDate=startDate,
                            endDate=endDate)
            
        return redirect('events-search')
    else:
        form = EventForm()
    return render(request, "main/events_add.html", {'form': form})

def calendar(request):
    current_user = request.user
    events = Event.objects.filter(users=current_user)
    context = {
        'events' : events
    }
    return render(request, "main/calendar.html", context)

