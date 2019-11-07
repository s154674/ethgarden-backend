from django.core.management.base import BaseCommand, CommandError
from customauth.models import User
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):

    def handle(self, *args, **options):
        # try:
        #     user = User.objects.get(pk=1)
        # except ObjectDoesNotExist as e:
        #     print('wowser')
        #     print(e)
        
        # print('some')

        user = User.objects.get(pk=2)
        print(user.has_usable_password())