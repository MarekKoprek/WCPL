from django.shortcuts import render

def profileHome(request):
    return render(request, 'main/profile_home.html')

def eventsSearch(request):
    return render(request, "main/events_search.html")

def calendar(request):
    return render(request, "main/calendar.html")
