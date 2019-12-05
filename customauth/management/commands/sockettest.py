from django.core.management.base import BaseCommand, CommandError
from customauth.models import User
from plants.models import Plant
from events.models import TransferEvent, GrownEvent
from django.core.exceptions import ObjectDoesNotExist
from web3.exceptions import BadFunctionCallOutput
from threading import Thread
import time
from web3 import Web3
import json

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
        print(event)
        try:
            plant = Plant.objects.get(plant_id=event['args']['plantId'])
            if (plant.seed == ""):
                plant.seed = event['args']['stats']
                plant.save()
        except ObjectDoesNotExist:
            print('plant not yet planted')
        
        
    def log_loop(self, event_filter, grown_filter, poll_interval, contract):
        for event in event_filter.get_all_entries():
            self.handle_transfer_event(event, contract)
        for event in grown_filter.get_all_entries():
            self.handle_grown_event(event)
        
        while True:
            for event in event_filter.get_new_entries():
                self.handle_transfer_event(event, contract)
            for event in grown_filter.get_new_entries():
                self.handle_grown_event(event)
            
            time.sleep(poll_interval)
            print("yes")

    def main(self, transfer_filter, grown_filter, contract):
        # block_filter = web3.eth.filter('latest')
        self.log_loop(transfer_filter, grown_filter, 2, contract)
 
    def handle(self, *args, **options):
        # print(Plant.objects.all().delete())
        web3 = Web3(Web3.WebsocketProvider('wss://ropsten.infura.io/ws/v3/d7a6df9d7430479b82c20fa9c462d964', websocket_kwargs={'timeout':60}))
        # web3.eth.defaultAccount = web3.eth.accounts[0]
        print("web3 is connected:", web3.isConnected())

        with open("C:/Users/johan/Projects/ethGarden.io/client/src/contracts/PlantBase.json") as plantbase:
            plantdict = json.load(plantbase)
            abi = plantdict['abi']
            plant_address = plantdict['networks']['5777']['address']

        plant_address = "0x25F7f77ce006C2F5BeC35d8D4a820e3Ad47f1d90"
        # print(abi)
    
        contract = web3.eth.contract(address=plant_address, abi=abi)
        transfer_filter = contract.events.Transfer.createFilter(fromBlock=6889000)
        grown_filter = contract.events.Grown.createFilter(fromBlock=6889000)
        
        self.main(transfer_filter, grown_filter, contract)
                



