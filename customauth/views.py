from django.shortcuts import render
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenViewBase
from customauth.serializers import ObtainTokenPairSerializer, SignatureObtainTokenPairSerializer, UserSerializer, GreenSeriazlizer
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from customauth.models import User
from plants.models import Plant
from events.models import BlockHeight
from customauth.custom_permission import OwnerOrReadOnly2


# Create your views here.
class ObtainTokenPairView(TokenViewBase):
    serializer_class = ObtainTokenPairSerializer

class SignatureObtainTokenPairView(generics.GenericAPIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = SignatureObtainTokenPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'public_address'

class GreenDetial(generics.RetrieveAPIView):
    # queryset = User.objects.get(public_address=self.kwargs['public_address'])
    permission_classes = (OwnerOrReadOnly2,)
    serializer_class = GreenSeriazlizer
    lookup_field = 'public_address'

    def get(self, request, *args, **kwargs):
        block_height = BlockHeight.objects.all().order_by("-pk")[0]
        user_pubkey = self.kwargs['public_address'] 
        user = User.objects.get(public_address=user_pubkey)
        plants = Plant.objects.filter(owner=user_pubkey)

        for plant in plants:
            if plant.last_green_calc < block_height.block_height:
                user.greens = user.greens + ((int(block_height.block_height) - int(plant.last_green_calc)) * plant.greens_per_block)
                plant.last_green_calc = block_height.block_height
                plant.save()
        user.save()

        return Response(self.get_serializer(user).data)
    
    def get_queryset(self):
        owner = self.kwargs['public_address']
        return User.objects.get(public_address=owner)
