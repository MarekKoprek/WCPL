from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('firm', 'Firm'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')
    picture = models.ImageField(default='user_icon.png', upload_to='profile_pictures')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    faculty = models.CharField(max_length=40, null=True, blank=True)
    course = models.CharField(max_length=50, null=True, blank=True)
    semester = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(7)], blank=True)
    nameFirm = models.CharField(max_length=50, default='Nokia', null=True, blank=True)
    website = models.CharField(max_length=100, default='https://www.nokia.com/', null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Event(models.Model):  
    picture = models.ImageField(default='default.jpg', upload_to='event_pics')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name="users_list", blank=True)
    addDate = models.DateTimeField(default=timezone.now)
    startDate = models.DateTimeField(default=timezone.now)
    endDate = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=620)
    accepted = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['startDate']
