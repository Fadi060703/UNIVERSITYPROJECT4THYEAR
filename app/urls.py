from django.urls import path 
from .views import ( ListCreateCityView , ListCreateLabView )
urlpatterns = [
    path( 'city' , ListCreateCityView.as_view() , name = 'CityListView' ) ,
    path( 'lab' , ListCreateLabView.as_view() , name = 'LabListView' ) ,
    
]
