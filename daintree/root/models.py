# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    STATUS_CHOICES = [
        ('seller', 'Seller'),
        ('buyer', 'Buyer'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,  default='buyer')

    objects = CustomUserManager()