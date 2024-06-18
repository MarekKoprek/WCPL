from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile, Event, Bug
from .forms import EventForm, ParticipationForm
from json import dumps
from datetime import datetime
from PIL import Image as PilImage
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
import os

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
            profile.picture = resize_uploaded_image(profile.picture, 200, 200)

        userInfo.save()
        profile.save()

        return redirect('profile-home', username=username)
    
    elif request.method == 'POST' and profile.user_type == 'firm':
        profile.nameFirm = request.POST.get('name', '')
        profile.website = request.POST.get('website', '')
        profile.bio = request.POST.get('bio', '')

        if 'picture' in request.FILES:
            profile.picture = request.FILES['picture']
            profile.picture = resize_uploaded_image(profile.picture, 200, 200)

        profile.save()

        return redirect('profile-home', username=username)

    context = {
        'userInfo' : userInfo,
        'profile' : profile,
        'userCurrent' : userCurrent
    }
    if username == "admin":
        if userCurrent.username != "admin":
            return redirect('profile-home', username=userCurrent.username)
        else:
            return redirect('login')

    if profile.user_type == 'student':
        return render(request, 'main/profile_home.html', context)
    else:
        return render(request, 'main/profile_firm.html', context)



@login_required
def eventsSearch(request):
    context = {
        'events': Event.objects.all(),
        'errorsCode': 0
        }
    return render(request, "main/events_search.html", context)

@login_required
def eventsInfo(request, id):
    currentEvent = get_object_or_404(Event, id=id)
    currentUser = request.user
    profiles = []
    for user in currentEvent.users.all():
        profile = Profile.objects.get(user=user)
        profiles.append(profile)
        
    isFound = False
    for user in currentEvent.users.all():
        if user.username == currentUser.username:
            isFound = True
    
    if request.method == 'POST':
        form = ParticipationForm(request.POST) 
        if currentUser.username != 'admin':
            if isFound:
                currentEvent.users.remove(currentUser)
            else:
                currentEvent.users.add(currentUser)
            currentEvent.save()
        
        return redirect('events-info', id=id)
    else:
        form = ParticipationForm()
        
    context = {
        'events': Event.objects.all(),
        'currentEvent': currentEvent,
        'currentUser': currentUser,
        'profiles': profiles,
        'ifParticipates': isFound,
        'errorsCode': 0,
        'form': form
    }
    return render(request, "main/events_info.html", context)

@login_required
def eventsAdd(request, errors):
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
        
        startDate = check_date(startDateList, startTimeList)
        if startDate == 1:
            startDate = datetime(int(startDateList[0]), int(startDateList[1]), int(startDateList[2]), int(startTimeList[0]), int(startTimeList[1]), 0)
        
        endDate = check_date(endDateList, endTimeList)
        if endDate == 1:
            endDate = datetime(int(endDateList[0]), int(endDateList[1]), int(endDateList[2]), int(endTimeList[0]), int(endTimeList[1]), 0)
        
        errors = check_errors(title, description, startDate, endDate)
        if errors != 0:
            return redirect('events-add', errors)
            
        if picture == None:
            newEvent = Event.objects.create(author=author, 
                            title=title, 
                            description=description, 
                            startDate=startDate,
                            endDate=endDate)
        else:   
            picture = resize_uploaded_image(picture, 200, 200)
            newEvent = Event.objects.create(author=author, 
                                picture=picture,
                                title=title, 
                                description=description, 
                                startDate=startDate,
                                endDate=endDate)
        newEvent.users.add(userCurrent)
        
        return redirect('events-search')
    else:
        errorsList = set_errors(errors)
        form = EventForm()

    context = {
        'errors': errorsList,
        'form': form
    }
    return render(request, "main/events_add.html", context)

@login_required
def eventsEdit(request, id, errors):
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
        
        startDate = check_date(startDateList, startTimeList)
        if startDate == 1:
            startDate = datetime(int(startDateList[0]), int(startDateList[1]), int(startDateList[2]), int(startTimeList[0]), int(startTimeList[1]), 0)
        
        endDate = check_date(endDateList, endTimeList)
        if endDate == 1:
            endDate = datetime(int(endDateList[0]), int(endDateList[1]), int(endDateList[2]), int(endTimeList[0]), int(endTimeList[1]), 0)
        
        errors = check_errors(title, description, startDate, endDate)
        if errors != 0:
            return redirect('events-edit', id, errors)
        
        if picture != None:
            picture = resize_uploaded_image(picture, 200, 200)
            currentEvent.picture = picture
        currentEvent.title = title
        currentEvent.description = description
        currentEvent.startDate = startDate
        currentEvent.endDate = endDate
        currentEvent.accepted = 0
        currentEvent.save()
        
        return redirect('events-search')
    else:
        errorsList = set_errors(errors)
        form = EventForm()
        
    context = {
        'currentEvent': currentEvent,
        'errors': errorsList,
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

@login_required
def bug(request):
    if request.method == 'POST':
        author = request.user
        section = request.POST.get('section')
        description = request.POST.get('description')

        newBug = Bug(author=author, section=section, description=description)
        newBug.save()

        return redirect('profile-home', username=author.username)

    return render(request, "main/bug.html")

def resize_uploaded_image(image, max_width, max_height):
    size = (max_width, max_height)

    if isinstance(image, InMemoryUploadedFile):
        memory_image = BytesIO(image.read())
        pil_image = PilImage.open(memory_image)
        img_format = os.path.splitext(image.name)[1][1:].upper()
        img_format = 'JPEG' if img_format == 'JPG' else img_format

        if pil_image.width > max_width or pil_image.height > max_height:
            pil_image.thumbnail(size)

        new_image = BytesIO()
        pil_image.save(new_image, format=img_format)

        new_image = ContentFile(new_image.getvalue())
        return InMemoryUploadedFile(new_image, None, image.name, image.content_type, None, None)

    elif isinstance(image, TemporaryUploadedFile):
        path = image.temporary_file_path()
        pil_image = PilImage.open(path)

        if pil_image.width > max_width or pil_image.height > max_height:
            pil_image.thumbnail(size)
            pil_image.save(path)
            image.size = os.stat(path).st_size

    return image

def set_errors(errorsCode):
    errors = []
    if errorsCode & (1 << 0):
        errors.append('Tytuł jest wymagany')
    if errorsCode & (1 << 1):
        errors.append('Tytuł nie może przekraczać 100 znaków')
    if errorsCode & (1 << 2):
        errors.append('Opis jest wymagany')
    if errorsCode & (1 << 3):
        errors.append('Opis nie może przekraczać 620 znaków')
    if errorsCode & (1 << 4):
        errors.append('Data ropoczęcia nie może być przed dzisiejszym dniem')
    if errorsCode & (1 << 5):
        errors.append('Data zakończenia nie może być przed datą rozpoczęcia')
    if errorsCode & (1 << 6):
        errors.append('Data ropoczęcia jest wymagana')
    if errorsCode & (1 << 7):
        errors.append('Data zakończenia jest wymagana')
    return errors

def check_errors(title, description, startDate, endDate):
    errorsCode = 0
    if len(title) == 0:
        errorsCode |= (1 << 0)
    if len(title) > 100:
        errorsCode |= (1 << 1)
    if len(description) == 0:
        errorsCode |= (1 << 2)
    if len(description) > 620:
        errorsCode |= (1 << 3)
    if startDate == 0:
        errorsCode |= (1 << 6)
    elif startDate < datetime.now():
        errorsCode |= (1 << 4)
    if endDate == 0:
        errorsCode |= (1 << 7)
    elif startDate != 0 and startDate > endDate:
        errorsCode |= (1 << 5)
    return errorsCode 

def check_date(dateList, timeList):
    for date in dateList:
        if len(date) == 0:
            return 0
    for time in timeList:
        if len(time) == 0:
            return 0
    return 1
