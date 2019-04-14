from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
import googlemaps

# gmaps = googlemaps.Client(key='')
# from delivery.api.location import get_lat_lon


class Branch(models.Model):
    name = models.CharField(null = True, max_length = 100)
    street = models.CharField(null = False, max_length = 100)
    city = models.CharField(null = False, max_length = 100)
    state = models.CharField(null = False, max_length = 100)
    lat = models.IntegerField(null = True, blank=True)
    lon = models.IntegerField(null = True, blank=True)

    # def create(self):
    #     address = self.street + ", " + self.city + ", " + self.state
    #     geocode_result = gmaps.geocode(address)
    #     lat = geocode_result[0]['geometry']['location']['lat']
    #     lon = geocode_result[0]['geometry']['location']['lng']
    #     self.lat = lat
    #     self.lon = lon

    def __unicode__(self):
        return self.name

    def get_address(self):
        address = self.street + ", " + self.city + ", " + self.state
        return address


class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    date = models.DateField(null = False)
    time = models.TimeField(null = False)
    number = PhoneNumberField(blank = True)
    place = models.ForeignKey(Branch,on_delete=models.CASCADE, null = False)
    details = models.CharField(null = True, max_length = 100)

    def __unicode__(self):
        text = self.user + "-" + self.date
        return text
