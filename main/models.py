from django.db import models
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
