from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from customauth.models import User
import json

class ObtainTokenPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        # data = super().validate(attrs)
        print(self.context['request'].user)
        user = self.context['request'].user
        print(user)
        print(self.context['request'].data)
        data = {'refresh' : '', 'access' : ''}
        refresh = self.get_token(user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data


class SignatureObtainTokenPairSerializer(serializers.Serializer):

    def validate(self, attrs):
        print('wow')
        signature = None
        request = self.context.get("request")
        signature = request.data.get('signature')
        if not signature:
            print('no signature')
            return None
        # try:
        #     signature = request.values('signature')
        #     print(signature)
        # except Exception as e:
        #     print(e)
        #     return None
        
        # user = self.context['request'].user
        user = User.objects.get(pk=1)
        
        refresh = RefreshToken.for_user(user)
        data = {'refresh' : '', 'access' : ''}
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data

