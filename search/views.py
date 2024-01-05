from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .models import Dishes,RestaurantDetails
import datetime
# Create your views here.

def searchDish(request):
    if request.method=='POST':
        dishName=request.POST['dish']
        restauranName=""
        restaurantName=request.POST['restaurant_name']
        results=[]
         # Perform the query
        if  dishName and restaurantName:
            # Filter dishes based on both dish name and restaurant name
            results = Dishes.objects.filter(item__icontains=dishName, restaurantDetails__name__icontains=restaurantName)
        elif dishName:
            # Filter dishes based on dish name only
            results = Dishes.objects.filter(item__icontains=dishName)
        elif restaurantName:
            # Filter dishes based on restaurant name only
            results = Dishes.objects.filter(restaurantDetails__name__icontains=restaurantName)
        else:
            # Both fields are empty, you might want to handle this case
            results = []
        return render(request,'searchAdmin.html',{ 'results' :results,'restaurantName':restaurantName})
    return render(request,'searchAdmin.html')



