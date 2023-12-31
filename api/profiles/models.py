from django.db import models
from django.contrib.auth.models import AbstractUser

from mesabite.base_models import TimeStampedModel
from profiles.managers import CustomUserManager


class User(AbstractUser, TimeStampedModel):
    username = None

    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email