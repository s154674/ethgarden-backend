from django.core.management.base import BaseCommand, CommandError
from customauth.models import User
from django.core.exceptions import ObjectDoesNotExist
from hexbytes import HexBytes
from web3 import Web3
from badges.models import Badge


class Command(BaseCommand):

    def handle(self, *args, **options):
        # web3 = Web3(Web3.WebsocketProvider('wss://ropsten.infura.io/ws/v3/d7a6df9d7430479b82c20fa9c462d964', websocket_kwargs={'timeout':60}))
        # # web3.eth.defaultAccount = web3.eth.accounts[0]
        # print("web3 is connected:", web3.isConnected())
        # # print(HexBytes('0xeebe07d0439b3f4838dd1d0a9fe3fd0ce3fe16ee572d4d6b9efae5768e68b405').hex())

        # owner = '0xf348328786984162e70f08d54a272427D810124b'
        # user = User.objects.get(public_address=owner)
        # things = []
        # print(user.userbadge_set.select_related())
        # for e in user.userbadge_set.select_related():
        #     print(str(e.badge_id.id))
        #     things.append(str(e.badge_id.id))
        
        # print(things)
        
        # objects = Badge.objects.filter(id__in=things)
        # print(objects)

        for user in User.objects.all():
            print(user.pk, user.public_address)
        