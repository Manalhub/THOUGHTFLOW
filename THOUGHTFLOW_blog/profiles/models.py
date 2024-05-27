from django.db import models
from django.contrib.auth.models import User

class Userprofile(models.Model):
    person = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    about = models.TextField()
    talks_about = models.CharField(max_length=250, default='anything')
    avatar = models.ImageField(upload_to='profile_photos', default='user.jpg')

    @property
    def avatar_url(self):
        """Return the URL of the user's avatar, or None if not available."""
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        return None

    def __str__(self):
        """Return a string representation of the user profile."""
        return f'Profile of {self.person.get_full_name()} last logged in at {self.person.last_login}'