from django.contrib import admin
from .models import RestaurantDetails,Dishes
# Register your models here.
@admin.register(RestaurantDetails)
class RestaurantDetails(admin.ModelAdmin):
    list_display=['ID','name','location','lat_long','other_details']
    
@admin.register(Dishes) 
class Dishes(admin.ModelAdmin):
    list_display=['item','price']   