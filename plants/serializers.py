from rest_framework import serializers, exceptions
from .models import Plant


class PlantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plant
        fields = ['plant_id', 'owner', 'seed', 'value', 'erc20_address', 'greens_per_block']

