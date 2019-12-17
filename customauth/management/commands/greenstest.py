from django.core.management.base import BaseCommand, CommandError
from customauth.models import User
from plants.models import Plant
from events.models import TransferEvent, GrownEvent, BlockHeight
from django.core.exceptions import ObjectDoesNotExist
from web3.exceptions import BadFunctionCallOutput
from threading import Thread
import time
from web3 import Web3
import json
from hexbytes import HexBytes
from datetime import datetime
import pytz

class Command(BaseCommand):
 
    def handle(self, *args, **options):
        block_height = BlockHeight.objects.all().order_by("-pk")[0]
        user_pubkey = "0xf348328786984162e70f08d54a272427D810124b" #HARDCODED FOR TESTING PURPOSES
        user = User.objects.get(public_address=user_pubkey)
        plants = Plant.objects.filter(owner=user_pubkey)
        
        # # TEST THINGS
        # user.greens = 0
        # for plant in plants:
        #     plant.last_green_calc = plant.plant_time
        #     plant.save()
        # # END TEST THINGS

        i= 1
        for plant in plants:
            print(f"{i} of {plants.count()}")
            i = i + 1
            if plant.last_green_calc < block_height.block_height:
                print(f'block descrepency: {int(block_height.block_height) - int(plant.last_green_calc)}')
                user.greens = user.greens + ((int(block_height.block_height) - int(plant.last_green_calc)) * plant.greens_per_block)
                plant.last_green_calc = block_height.block_height
                plant.save()
                print(f"user greens: {user.greens}")
        user.save()
            
        

