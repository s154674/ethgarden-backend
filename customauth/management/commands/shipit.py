import json
import os
import sys

from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.db.models import IntegerField
from django.db.models.functions import Cast
from django.shortcuts import render
from eth_keys import keys
from hexbytes import HexBytes
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from web3 import Web3

from badges.models import Badge
from customauth.custom_permission import OwnerOrReadOnly, OwnerOrReadOnly2
from customauth.models import User
# from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from plants.models import Plant
# from rest_framework_simplejwt.views import TokenViewBase
from plants.serializers import PlantSerializer


class Command(BaseCommand):

    def handle(self, *args, **options):
        web3 = Web3(Web3.WebsocketProvider('wss://ropsten.infura.io/ws/v3/d7a6df9d7430479b82c20fa9c462d964', websocket_kwargs={'timeout':60}))

        with open(os.path.join(sys.path[0], 'PlantBase.json')) as plantbase:
            plantdict = json.load(plantbase)
            abi = plantdict['abi']
            
        plant_address = "0x25F7f77ce006C2F5BeC35d8D4a820e3Ad47f1d90"
    
        plantbase = web3.eth.contract(address=plant_address, abi=abi)

        nonce = web3.eth.getTransactionCount('0xf348328786984162e70f08d54a272427D810124b')
        
        i = 0
        for plant in Plant.objects.filter(seed="").exclude(owner="0x0000000000000000000000000000000000000000"):
            token_id = int(plant.pk)
            print(token_id)

            shipIt_txn = plantbase.functions.shipIt(token_id).buildTransaction({
                'chainId': 3,
                'gas': 100000, 
                'gasPrice': web3.toWei('1', 'gwei'), # TODO Determin gasprice in realtime
                'nonce': nonce + i,
            })
            i = i + 1
            # print(shipIt_txn)

            private_key = web3.toBytes(hexstr='EEC0C835143A7376D426D5CD4DAAC0B9524A8BF983B8430346D7051EC163A39F')
            # print(private_key)
            signed_txn = web3.eth.account.sign_transaction(shipIt_txn, private_key=private_key)
            # print(signed_txn.hash)
            web3.eth.sendRawTransaction(signed_txn.rawTransaction)
