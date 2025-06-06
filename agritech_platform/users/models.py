from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    role = models.CharField(
        max_length=10, 
        choices=[('farmer', 'Farmer'), ('investor', 'Investor')]
    )