from django.db import models
from customauth.models import User

# Create your models here.
class Badge(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()


class UserBadge(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    badge_id = models.ForeignKey(Badge, related_name='badges', on_delete=models.CASCADE)
