from django.shortcuts import render

def profileHome(request):
    return render(request, 'main/profile_home.html')

events = [
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
        'events': events,
        'participantRows': participantRows
        }
    return render(request, "main/events_search.html", context)

def eventsAdd(request):
    return render(request, "main/events_add.html")

def calendar(request):
    return render(request, "main/calendar.html")
