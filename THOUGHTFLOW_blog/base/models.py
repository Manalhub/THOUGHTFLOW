from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Post(models.Model):
    id = models.UUIDField(primary_key=True, max_length=15, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='created', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='bg_img/', default='default_bg_img.jpg')
    category = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def images_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['created'])]

    def __str__(self) -> str:
        return self.title
    
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    id = models.UUIDField(primary_key=True, max_length=15,
    editable=False, default=uuid.uuid4)
    author = models.CharField(max_length=80)
    comment_p = models.ForeignKey(Post, on_delete=models.CASCADE,
    related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    eddited = models.DateTimeField(auto_now=True)
    signedup_user = models.ForeignKey(User, on_delete=models.CASCADE,
    null=True, blank=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.comment_p}"