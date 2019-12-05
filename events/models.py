from django.db import models

# Create your models here.
class TransferEvent(models.Model):
    from_address = models.CharField(max_length=42)
    to_address = models.CharField(max_length=42)
    plant_id = models.CharField(max_length=78) # Character length of 2^256 
    block_number = models.CharField(max_length=78)
    transaction_hash = models.CharField(max_length=66) # 64 nibbles in hex + 0x prefix

    class Meta:
        indexes = [
            models.Index(fields=['block_number']),
            models.Index(fields=['transaction_hash']),
            models.Index(fields=['plant_id']),
            models.Index(fields=['from_address']),
            models.Index(fields=['to_address'])
        ]


class GrownEvent(models.Model):
    plant_id = models.CharField(max_length=78)
    seed = models.CharField(max_length=78)
    block_number = models.CharField(max_length=78)
    transaction_hash = models.CharField(max_length=66)

    class Meta:
        indexes = [
            models.Index(fields=['block_number']),
            models.Index(fields=['transaction_hash']),
            models.Index(fields=['plant_id'])
        ]