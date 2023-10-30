from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=256)
    adress = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    rating = models.DecimalField(decimal_places=2, max_digits=5)
    
    def __str__(self):
        return f'{self.name}'