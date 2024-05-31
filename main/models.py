from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    faculty = models.CharField(max_length=40)
    course = models.CharField(max_length=50)
    semester = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.user.username

class Event(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name="users_list", blank=True)
    addDate = models.DateTimeField(default=timezone.now)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['startDate']
