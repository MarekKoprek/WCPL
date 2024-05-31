from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('profile/<str:username>', views.profileHome, name='profile-home'),
    path('events/', views.eventsSearch, name='events-search'),
    path('events/<int:id>', views.eventsInfo, name='events-info'),
    path('calendar/', views.calendar, name='calendar'),
    path('events/add', views.eventsAdd, name='events-add'),
    path('register/', user_views.register, name='register'),
]