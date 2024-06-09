from django.urls import path
from . import views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('profile/<str:username>', views.profileHome, name='profile-home'),
    path('events/', views.eventsSearch, name='events-search'),
    path('events/<int:id>', views.eventsInfo, name='events-info'),
    path('events/edit/<int:id>', views.eventsEdit, name='events-edit'),
    path('calendar/', views.calendar, name='calendar'),
    path('events/add', views.eventsAdd, name='events-add'),
    path('register/', user_views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('bug/', views.bug, name='bug')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

