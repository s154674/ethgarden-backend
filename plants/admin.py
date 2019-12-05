from django.contrib import admin
from plants.models import Plant

# Register your models here.
class PlantAdmin(admin.ModelAdmin):
    pass

admin.site.register(Plant, PlantAdmin)