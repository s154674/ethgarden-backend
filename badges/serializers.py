from rest_framework import serializers, exceptions
from .models import Badge, UserBadge


class BadgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Badge
        fields = ['id', 'name', 'price']


# class UserBadgeSerializer(serializers.ModelSerializer):
#     # badges = serializers.StringRelatedField(many=True)

#     class Meta:
#         model = Badge
#         fields = ['pk', 'name', 'price']

class ClaimBadgeSerializer(serializers.ModelSerializer):
    
    # def validate(self, attrs):
    #     user_id, badge_id = None, None
    #     request = self.context.get("request")
    #     user_id = request.data.get('user_id')
    #     badge_id = request.data.get('badge_id')
    #     if not user_id or not badge_id:
    #         raise exceptions.AuthenticationFailed(detail="user_id and badge_id fields are required", code=400)
            
    #     data = {'user_id' : '', 'badge_id' : ''}
    #     data['user_id'] = user_id
    #     data['badge_id'] = badge_id

    #     return data
    
    class Meta:
        model = UserBadge
        fields = ['user_id', 'badge_id']