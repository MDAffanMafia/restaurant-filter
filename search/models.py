from django.db import models

#model for retaurant Details
class RestaurantDetails(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    lat_long = models.CharField(max_length=200)
    other_details = models.JSONField()

class Dishes(models.Model):
    restaurantDetails = models.ForeignKey(RestaurantDetails, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
