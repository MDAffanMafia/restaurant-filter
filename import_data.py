import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurantSearch.settings")
import django
django.setup()
import csv,json
from django.core.management.base import BaseCommand
from search.models import RestaurantDetails,Dishes
def handle():
        print("the data is")
        csv_file_path = 'restaurantFinal.csv'  # Update with the actual path
        with open(csv_file_path, 'r') as csvfile:
            print("the data is importing")
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                restaurant_data = {
                    'ID': row[0],
                    'name': row[1],
                    'location': row[2],
                    'lat_long': row[4],
                    'other_details': row[5],
                }
                RestaurantDetails.objects.create(**restaurant_data)
        csv_file_path = 'restaurantFinal.csv'  # Update with the actual path
        with open(csv_file_path, 'r') as csvfile:
            print("the data is importing")
            reader = csv.reader(csvfile)
            next(reader)
            allDishes=[]
            for row in reader:
                  allItems = json.loads(row[3])
                  allItems = list(allItems.items())
                  ID = RestaurantDetails.objects.get(ID=row[0])
                  restaurantMenu=[]
                  for item in allItems:
                    allDishes+=[(Dishes(restaurantDetails=ID, item=item[0], price=item[1]))]
            Dishes.objects.bulk_create(allDishes)          
            

        print("the data imported succesfully")
if __name__ == "__main__":
    handle()        