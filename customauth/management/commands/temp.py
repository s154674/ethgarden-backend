from django.core.management.base import BaseCommand, CommandError
from customauth.models import User
from django.core.exceptions import ObjectDoesNotExist
from hexbytes import HexBytes

class Command(BaseCommand):

    def handle(self, *args, **options):
        if (None == ""): 
            print('dasda')
        else: 
            print('eeee')
        # print(HexBytes('0xeebe07d0439b3f4838dd1d0a9fe3fd0ce3fe16ee572d4d6b9efae5768e68b405').hex())