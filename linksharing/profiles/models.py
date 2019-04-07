from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    photo = models.ImageField(upload_to='user', default='linksharing/static/img/default.png')


