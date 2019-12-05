from rest_framework import permissions
from customauth.models import User

class OwnerOrReadOnly(permissions.BasePermission):
    message = 'You can only lookup your own plants'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            print('adank')
            print(request.query_params)
            print(request.user.public_address)
            return True
        else:
            print(request.query_params)
            print(request.user.public_address)
            return False

    def has_object_permission(self, request, view, obj):
        return False