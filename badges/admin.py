from django.contrib import admin
from badges.models import Badge, UserBadge

# Register your models here.
class BadgeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Badge, BadgeAdmin)

class UserBadgeAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserBadge, UserBadgeAdmin)