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
import sys, os

class Command(BaseCommand):

    def handle_transfer_event(self, event, contract):
        # print('Something')
        # print(event)
        # print(event['args']['from'])
        try:
            # Case 1: Plant already exists and changes ownership
            plant = Plant.objects.get(plant_id=event['args']['tokenId'])
            plant.owner = event['args']['to']
            plant.save()
        except ObjectDoesNotExist: # Cannot get plant, not in database
            try:
                # Get plant attributes (List of length 4 with indexes corresponding to seed, value, plantTime and erc20 address in that order)
                plant_list = contract.functions.plants(event['args']['tokenId']).call()
            except BadFunctionCallOutput:
                # TODO Handle: What to do if you cant find the plant in the smart contract? Should not happen
                pass

            # Case 2: Create a new plant entry for the transfer event
            if (event['args']['from'] == '0x0000000000000000000000000000000000000000'):
                plant = Plant(plant_id=event['args']['tokenId'],
                owner=event['args']['to'],
                last_green_calc=event['blockNumber'],
                value=plant_list[1],
                plantTime=plant_list[2],
                erc20_address=plant_list[3])
                plant.save()
            else:
                # TODO Handle: You cant find it in the database + the sender is not 0 address
                pass
        
        # except Exception as e:
        #     # TODO Return internal server error
        #     pass

    def handle_grown_event(self, event):
        try:
            plant = Plant.objects.get(plant_id=event['args']['plantId'])
            if (plant.seed == ""):
                plant.seed = int(event['args']['stats'])
                plant.save()
            else:
                pass # GrownEvent already handled
        except ObjectDoesNotExist:
            print('plant not yet planted')
        
        
    def log_loop(self, transfer_filter, grown_filter, poll_interval, contract, web3):
        # Rerun existing entries + get block height
        for event in transfer_filter.get_all_entries():
            self.handle_transfer_event(event, contract)
        
        for event in grown_filter.get_all_entries():
            self.handle_grown_event(event)
        
        latest_block = web3.eth.getBlock('latest')
        if not BlockHeight.objects.all():
            block_height = self.handle_new_block(web3, latest_block)
        else:
            block_height = BlockHeight.objects.all().order_by("-pk")[0]
        
        # Check for new stuff periodically
        while True:
            for event in transfer_filter.get_new_entries():
                self.handle_transfer_event(event, contract)
            for event in grown_filter.get_new_entries():
                self.handle_grown_event(event)
            
            latest_block = web3.eth.getBlock('latest')
            if int(block_height.block_height) < latest_block.number:
                block_height = self.handle_new_block(web3, latest_block)
            
            time.sleep(poll_interval)
            print("yes") # TODO something else to handle livelyness

    def main(self, transfer_filter, grown_filter, contract, web3):
        # block_filter = web3.eth.filter('latest')
        self.log_loop(transfer_filter, grown_filter, 2, contract, web3)

    def handle_new_block(self, web3, latest_block):
        block_height = BlockHeight(block_height=latest_block.number, time=datetime.utcfromtimestamp(latest_block.timestamp).replace(tzinfo=pytz.utc), block_hash=HexBytes(latest_block.hash).hex())
        block_height.save()
        return block_height

 
    def handle(self, *args, **options):
        web3 = Web3(Web3.WebsocketProvider('wss://ropsten.infura.io/ws/v3/d7a6df9d7430479b82c20fa9c462d964', websocket_kwargs={'timeout':60}))
        
        print("web3 is connected:", web3.isConnected())

        with open(os.path.join(sys.path[0], 'PlantBase.json')) as plantbase:
            plantdict = json.load(plantbase)
            abi = plantdict['abi']
            plant_address = plantdict['networks']['5777']['address']

        plant_address = "0x25F7f77ce006C2F5BeC35d8D4a820e3Ad47f1d90"
        # print(abi)
    
        contract = web3.eth.contract(address=plant_address, abi=abi)
        transfer_filter = contract.events.Transfer.createFilter(fromBlock=6889000)
        grown_filter = contract.events.Grown.createFilter(fromBlock=6889000)
        
        self.main(transfer_filter, grown_filter, contract, web3)
                



