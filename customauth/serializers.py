from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers, exceptions
from customauth.models import User
import json
from .signature_check import Address
from django.core.exceptions import ObjectDoesNotExist


class ObtainTokenPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        user = self.context['request'].user
        data = {'refresh' : '', 'access' : ''}
        refresh = self.get_token(user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data


class SignatureObtainTokenPairSerializer(serializers.Serializer):

    def validate(self, attrs):
        signature, nonce = None, None
        request = self.context.get('request')
        signature = request.data.get('signature')
        nonce = request.data.get('nonce')
        address = request.data.get('address')
        if not signature or not nonce:
            raise exceptions.AuthenticationFailed(detail="signature and nonce fields required", code=400)
            
        # Get address from signature and nonce
        address_from_sig = Address.fromSignatureAndNonce(self, signature=signature, nonce=nonce)
        #TODO Do a check that it's a valid ethereum address 
        if not address == address_from_sig:
            raise exceptions.AuthenticationFailed(detail="Address returned from signature check is not right", code=400)

        # Retrive user with that address, or create a new user with that address
        try: 
            user = User.objects.get(public_address=address)
        except ObjectDoesNotExist:
            user = User.objects.create_user(username=address, public_address=address)
            user.save()
            user.set_unusable_password()
            user.save()

        # Checking nonce provided is the same as users
        if not user.nonce == int(nonce):
            raise exceptions.AuthenticationFailed(detail="nonce missmatch", code=400)
        
        # Increment user nonce 
        # TODO Uncomment this when the rest of the infrastructure is there
        # user.nonce = user.nonce + 1
        # user.save()
        
        refresh = RefreshToken.for_user(user)
        data = {'refresh' : '', 'access' : ''}
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'public_address', 'nonce']

class GreenSeriazlizer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['greens']