from django.db import models
from django.contrib.auth.models import AbstractUser

# class Lead(models.Model):
#     SOURCE_CHOICES = (
#         ('Youtube', 'Youtube'),
#         ('Google', 'Google'),
#         ('Newsletter', 'Newsletter')
#     )
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     age = models.IntegerField(default=0)
#     phoned = models.BooleanField(default=False)
#     source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
#     profile_picture = models.ImageField(blank=True, null=True)
#     special_files = models.FileField(blank=True, null=True)

class User(AbstractUser):
    pass

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    # every lead have 1 Agent 
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)  

class Agent(models.Model):
    # every lead have 1 User 
    user = models.ForeignKey(User, on_delete=models.CASCADE)


