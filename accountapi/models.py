from django.db import models
from django.contrib.auth.models import AbstractUser
from accountapi.managers import CustomUserManager
roleChoices = [
    ("ADMIN", "Admin"),
    ("USER","User")
]

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    role = models.CharField(max_length=255, choices=roleChoices, default="USER")
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']