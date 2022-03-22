from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    # every lead have 1 Agent 
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Agent(models.Model):
    # every lead have 1 User 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

# Signal

def post_user_created_signal(sender, instance, created, **kwargs):
    # TODO: if create new User, signal will send and auto create new UserProfile of User
    """_summary_

    Args:
        sender (_type_): _description_
        instance (_type_): return username(email,...) of user if save data
        created (_type_): return True or Fasle if user create new data
    """
    # print(instance, created)
    if created: 
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)

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
