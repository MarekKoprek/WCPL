from django.shortcuts import render

def profileHome(request):
    return render(request, 'main/profile_home.html')
