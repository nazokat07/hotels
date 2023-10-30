from django.contrib import admin
from .models import *

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'number')
    list_display_links = ('id', 'number')
    ordering = ('number',)


