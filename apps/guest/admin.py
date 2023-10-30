from django.contrib import admin
from .models import *

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname')
    list_display_links = ('id', 'firstname')
    ordering = ('firstname',)

