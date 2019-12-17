from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from customauth.custom_permission import OwnerOrReadOnly
from rest_framework import generics, status, permissions, exceptions
from rest_framework.response import Response
# from rest_framework_simplejwt.views import TokenViewBase
from badges.serializers import BadgeSerializer, ClaimBadgeSerializer
# from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from badges.models import Badge, UserBadge
from customauth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class BadgeList(generics.ListAPIView, APIView):
    permission_classes = (OwnerOrReadOnly,)
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer


class UserBadgeList(generics.ListAPIView, APIView):
    permission_classes = (OwnerOrReadOnly,)
    # queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    lookup_field = 'owner'

    def get_queryset(self):
        owner = self.kwargs['owner']
        user = User.objects.get(public_address=owner)
        things = []
        for e in user.userbadge_set.select_related():
            things.append(str(e.badge_id.id))
        
        return Badge.objects.filter(id__in=things)
      

class ClaimBadge(generics.GenericAPIView):
    # permission_classes = (OwnerOrReadOnly,)
    serializer_class = ClaimBadgeSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            owner = str(request.user.public_address)
            user = User.objects.get(public_address=owner)
            badge = Badge.objects.get(pk=int(request.data.get('badge_id')))

            if not int(request.data.get('user_id')) == int(user.pk):
                raise exceptions.AuthenticationFailed(detail="A User can only claim badges for the user themselves", code=403)

            print(user.greens, badge.price)
            if user.greens < badge.price:
                raise exceptions.AuthenticationFailed(detail="Not enough greens to claim badge", code=402)
            
            # things = []
            # for e in user.userbadge_set.select_related():
            #     things.append(str(e.badge_id.id))

            try:
                UserBadge.objects.get(user_id=user, badge_id=badge)
            except ObjectDoesNotExist:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            raise exceptions.AuthenticationFailed(detail="Badge already claimed", code=400) 
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    