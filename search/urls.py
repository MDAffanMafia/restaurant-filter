from django.urls import path
from search import views
urlpatterns = [
    path('searchDish',views.searchDish,name='searchDish'),
]