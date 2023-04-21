from django.contrib import admin
from .models import KitchenRequest


class KitchenRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'type', 'height', 'size', 'style', 'fasad', 'stoleshnica', 'furnitura']
    search_fields = ['name', 'phone']
    list_filter = ['type', 'height', 'size', 'style', 'fasad', 'stoleshnica', 'furnitura']


admin.site.register(KitchenRequest, KitchenRequestAdmin)
