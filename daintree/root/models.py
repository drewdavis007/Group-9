from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    STATUS_CHOICES = [
        ('seller', 'Seller'),
        ('buyer', 'Buyer'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='buyer')

    # add additional fields here
    objects = CustomUserManager()
