from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Character(models.Model):
    player = models.OneToOneField(User)
    experience = models.IntegerField()
    action = models.IntegerField()
    avatar = models.ImageField(upload_to='upload/',null=True,blank=True)
    title = models.CharField(max_length=255,default='Newbie') 

    def __str__(self):
        return self.player.username

class Action(models.Model):
    action = models.IntegerField()
    experience = models.IntegerField()
    description = models.CharField(max_length=255)
        
    def __str__(self):
        return self.description


class ActionLog(models.Model):
    player = models.ForeignKey(Character)
    action = models.ForeignKey(Action)
    dt = models.DateTimeField(auto_now_add=True)


class Reward(models.Model):
    attr = models.CharField(max_length=255)
    point = models.IntegerField()
    inc = models.BooleanField()
    img = models.ImageField(upload_to='upload/',null=True,blank=True)
    inf = models.BooleanField()
    limit = models.IntegerField()
    str_val = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self):
        if not self.description:
            return "None"
        return self.description


class RewardLog(models.Model):
    player = models.ForeignKey(Character)
    reward = models.ForeignKey(Reward)
    dt = models.DateTimeField(auto_now_add=True)


class RewardCondition(models.Model):
    CONDITION_CHOICE = (
        ('lt','Less Than'),
        ('gt','Greater Than'),
        ('eq','Equal'),
        ('leq','Less and Equal'),
        ('geq','Greater and Equal'),
    )
    
    action = models.ForeignKey(Action)
    reward = models.ForeignKey(Reward)
    counter = models.IntegerField()
    condition = models.CharField(max_length=3,choices=CONDITION_CHOICE)
    
    def __str__(self):
        return self.reward.description
