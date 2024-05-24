from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    biography = models.TextField()
    interests = models.CharField(max_length=250, default='anything')

    def __str__(self):
        return f'Profile of {self.user.first_name} last logged in at {self.user.last_login}'
