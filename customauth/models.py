from django.db import models
from django.contrib.auth.models import AbstractUser

# Adding a custom user for future editting
class User(AbstractUser):
    public_address = models.CharField(max_length=140, unique=True)
    nonce = models.IntegerField(default=1)
    greens = models.PositiveIntegerField(default=0)
