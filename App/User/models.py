from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager
from django.forms import PasswordInput


class User(AbstractUser):
    username = None

    worker_id = models.CharField(
        verbose_name='Worker ID',
        max_length=255,
        unique=True
    )
    first_name = models.CharField(
        verbose_name='First name',
        max_length=255,
    )
    last_name = models.CharField(
        verbose_name='Last name',
        max_length=255,
    )
    email = models.EmailField(
        verbose_name='Email address',
        unique=True
    )
    avatar = models.ImageField(
        verbose_name='Avatar',
    )
    USERNAME_FIELD = 'worker_id'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.worker_id

    class Meta:
        ordering = ['id']
        