from django.db import models
from apps.room.models import Room
from apps.guest.models import Guest

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
    ispaid = models.BooleanField()
    
    def __str__(self):
        return f'{self.room}'