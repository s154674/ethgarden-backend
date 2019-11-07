from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenViewBase
from customauth.serializers import ObtainTokenPairSerializer, SignatureObtainTokenPairSerializer, UserSerializer
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from customauth.models import User


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