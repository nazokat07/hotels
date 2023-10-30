from django.contrib import admin
from .models import *

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'room')
    list_display_links = ('id', 'room')
    ordering = ('room',)


