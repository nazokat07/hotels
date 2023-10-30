from django.db import models

class Guest(models.Model):
    firstname = models.CharField(max_length=256)
    lastname = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    phonenumber = models.CharField(max_length=256)
    
    def __str__(self):
        return f'{self.firstname}'
