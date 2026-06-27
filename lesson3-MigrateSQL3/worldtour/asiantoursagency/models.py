from django.db import models

# Create your models here.
class Tour(models.Model):
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return (f"origin_country: {self.origin_country}, destination_country: {self.destination_country}, numbers_of_nights: {self.number_of_nights}, price_per_night: {self.price}")