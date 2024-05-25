from django.db import models
from django.contrib.auth.models import User

class Userprofile(models.Model):
    person = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    about = models.TextField()
    talks_about = models.CharField(max_length=250, default='anything')
    avatar = models.ImageField(upload_to='profile_photos', default='user.jpg')

    def __str__(self):
        return f'Profile of {self.person.first_name} last logged in at {self.person.last_login}'
