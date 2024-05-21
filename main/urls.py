from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>', views.profileHome, name='profile-home'),
    path('events/', views.eventsSearch, name='events-search'),
    path('calendar/', views.calendar, name='calendar')
]