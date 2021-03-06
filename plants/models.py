from django.db import models
# from customauth.models import User

# Create your models here.
class Plant(models.Model):
    plant_id = models.CharField(max_length=78, primary_key=True, unique=True)
    owner = models.CharField(max_length=42)
    # owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    last_green_calc = models.CharField(max_length=78)
    plant_time = models.CharField(max_length=78)
    seed = models.CharField(max_length=78, default="")
    value = models.CharField(max_length=78)
    erc20_address = models.CharField(max_length=42)
    greens_per_block = models.SmallIntegerField(default=10)

    class Meta:
        indexes = [
            models.Index(fields=['owner']),
            models.Index(fields=['erc20_address']),
            models.Index(fields=['plant_id'])
        ]