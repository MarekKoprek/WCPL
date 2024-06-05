from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile, Event
from .forms import EventForm, ParticipationForm
from json import dumps
from datetime import datetime

@login_required
def profileHome(request, username):
    userInfo = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=userInfo)
    userCurrent = request.user

    if request.method == 'POST' and profile.user_type == 'student':
        userInfo.first_name = request.POST.get('first_name', '')
        userInfo.last_name = request.POST.get('last_name', '')
        userInfo.email = request.POST.get('email', '')

        profile.phone_number = request.POST.get('phone_number', '')
        profile.faculty = request.POST.get('faculty', '')
        profile.course = request.POST.get('course', '')
        profile.semester = request.POST.get('semester', '')
        profile.bio = request.POST.get('bio', '')

        if 'picture' in request.FILES:
            profile.picture = request.FILES['picture']

        userInfo.save()
        profile.save()

        return redirect('profile-home', username=username)
    
    elif request.method == 'POST' and profile.user_type == 'firm':
        profile.nameFirm = request.POST.get('name', '')
        profile.website = request.POST.get('website', '')
        profile.bio = request.POST.get('bio', '')

        if 'picture' in request.FILES:
            profile.picture = request.FILES['picture']

        profile.save()

        return redirect('profile-home', username=username)

    context = {
        'userInfo' : userInfo,
        'profile' : profile,
        'userCurrent' : userCurrent
    }

    if profile.user_type == 'student':
        return render(request, 'main/profile_home.html', context)
    else:
        return render(request, 'main/profile_firm.html', context)



@login_required
def eventsSearch(request):
    context = {
        'events': Event.objects.all(),
        }
    return render(request, "main/events_search.html", context)

@login_required
def eventsInfo(request, id):
    currentEvent = get_object_or_404(Event, id=id)
    currentUser = request.user
    print(currentEvent.users.all)
    
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
        'currentUser': currentUser,
        'form': form
    }
    return render(request, "main/events_info.html", context)

@login_required
def eventsAdd(request):
    userCurrent = request.user
    
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        author = userCurrent
        picture = request.FILES.get('picture')
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
        
        now = datetime.now()
        if(startDate > endDate or startDate < now):
            return redirect('events-add')
            
        Event.objects.create(author=author, 
                            picture=picture,
                            title=title, 
                            description=description, 
                            startDate=startDate,
                            endDate=endDate)
            
        return redirect('events-search')
    else:
        form = EventForm()
    return render(request, "main/events_add.html", {'form': form})

@login_required
def eventsEdit(request, id):
    currentEvent = get_object_or_404(Event, id=id)
    currentUser = request.user
    
    if currentEvent.author != currentUser:
        return redirect('events-search')
    
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        picture = request.FILES.get('picture')
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
        
        now = datetime.now()
        if(startDate > endDate or startDate < now):
            return redirect('events-edit', id=id)
        
        currentEvent.picture = picture
        currentEvent.title = title
        currentEvent.description = description
        currentEvent.startDate = startDate
        currentEvent.endDate = endDate
        currentEvent.accepted = 0
        currentEvent.save()
        
        return redirect('events-search')
    else:
        form = EventForm()
        
    context = {
        'currentEvent': currentEvent,
        'form': form
    }
    
    return render(request, "main/events_edit.html", context)

@login_required
def calendar(request):
    current_user = request.user
    events = Event.objects.filter(users=current_user)
    context = {
        'events' : events
    }
    return render(request, "main/calendar.html", context)

