from django.shortcuts import render
from customauth.custom_permission import OwnerOrReadOnly
from rest_framework import generics, status, permissions
from rest_framework.response import Response
# from rest_framework_simplejwt.views import TokenViewBase
from plants.serializers import PlantSerializer
# from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from plants.models import Plant
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class PlantList(generics.ListAPIView, APIView):
    permission_classes = (OwnerOrReadOnly,)
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    lookup_field = 'owner'

    def get_queryset(self):
        owner = self.kwargs['owner']
        return Plant.objects.filter(owner=owner)