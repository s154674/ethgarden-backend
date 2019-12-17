from rest_framework import permissions
from customauth.models import User

class OwnerOrReadOnly(permissions.BasePermission):
    message = 'You can only lookup your own plants'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # Safe methods are allowed
            return True
        else:
            # print(request.query_params)
            # print(request.user.public_address)
            return view.kwargs['owner'] == str(request.user.public_address)

    def has_object_permission(self, request, view, obj):
        return False


class OwnerOrReadOnly2(permissions.BasePermission):
    message = 'You can only lookup your own plants'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # Safe methods are allowed
            return True
        else:
            # print(request.query_params)
            # print(request.user.public_address)
            return view.kwargs['owner'] == str(request.user.public_address)

    # def has_object_permission(self, request, view, obj):
    #     return False