from django.urls import path 
from .views import ( ListCreateCityView , ListCreateLabView , RetrieveCityView , RetrieveLabView  ,
                    ListCreatePharmacyView , RetrievePharmacyView , ListCreateCategoryView ,
                    RetrieveCategoryView , ListCreateProductView , RetrieveProductView ) 
urlpatterns = [
    path( 'city' , ListCreateCityView.as_view() , name = 'CityListView' ) ,
    path( 'city/<int:pk>' , RetrieveCityView.as_view() , name = 'CityView' ) ,
    path( 'lab' , ListCreateLabView.as_view() , name = 'LabListView' ) ,
    path( 'lab/<int:pk>' , RetrieveLabView.as_view() , name = 'LabView' ) ,
    path( 'pharm' , ListCreatePharmacyView.as_view() , name = 'PharmListView' ) ,
    path( 'pharm/<int:pk>' , RetrievePharmacyView.as_view() , name = 'PharmView' ) ,
    path( 'categ' , ListCreateCategoryView.as_view() , name = 'CategListView' ) ,
    path( 'categ/<int:pk>' , RetrieveCategoryView.as_view() , name = 'CategView' ) ,
    path( 'prod' , ListCreateProductView.as_view() , name = 'ProdListView' ) ,
    path( 'prod/<int:pk>' , RetrieveProductView.as_view() , name = 'ProdView' ) 
]
