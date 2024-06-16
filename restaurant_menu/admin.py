from django.contrib import admin
from .models import Item

class MenuItemAdmin(admin.ModelAdmin):
    # admin setup/config options
    list_display = ("meal", "status")
    list_filter = ("status", )
    search_fields = ("meal", "description")

# registers this in connection with Item class from models
admin.site.register(Item, MenuItemAdmin)
