from django.contrib import admin
from events.models import GrownEvent, TransferEvent, BlockHeight

# Register your models here.
class GrownEventAdmin(admin.ModelAdmin):
    pass

class TransferEventAdmin(admin.ModelAdmin):
    pass

class BlockHeightAdmin(admin.ModelAdmin):
    pass


admin.site.register(GrownEvent, GrownEventAdmin)
admin.site.register(TransferEvent, TransferEventAdmin)
admin.site.register(BlockHeight, BlockHeightAdmin)
