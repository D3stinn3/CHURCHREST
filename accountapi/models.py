from django.db import models
from django.contrib.auth.models import AbstractUser
from eventapi.models import Event

roleChoices = [
    ("ADMIN", "Admin"),
    ("USER","User")
]

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    role = models.CharField(max_length=255, choices=roleChoices, default="USER")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']