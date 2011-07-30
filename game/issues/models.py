from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Issue(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/upload/',null=True,blank=True)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    user = models.ForeignKey(User)
     
