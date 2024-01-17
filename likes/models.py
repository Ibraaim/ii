from django.db import models
from django.contrib.auth.models import User
class Video(models.Model):
         likes = models.ManyToManyField(User, blank=True, related_name='likes')
         dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')
