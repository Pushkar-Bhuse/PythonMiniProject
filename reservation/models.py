from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from delivery.api.la


class Branch(models.Model):
    name = models.CharField(null = True, max_length = 100)
    street = models.CharField(null = False, max_length = 100)
    city = models.CharField(null = False, max_length = 100)
    state = models.CharField(null = False, max_length = 100)
    lat = models.IntegerField(null = True, blank=True)
    lon = models.IntegerField(null = True, blank=True)

    def create(self):



class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    date = models.DateField(null = False)
    time = models.TimeField(null = False)
    number = PhoneNumberField(blank = True)
    place = models.ForeignKey(Branch,on_delete=models.CASCADE, null = False)
    details = models.CharField(null = True, max_length = 100)