from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')

    def __str__(self) :
        return self.username