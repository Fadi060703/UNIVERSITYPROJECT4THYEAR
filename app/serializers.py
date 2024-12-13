from rest_framework import serializers 
from .models import ( City , Lab , Pharmacy , Category , Product , Storage , 
                     MainStorageOfProducts , PharmacyStorageOfProducts , 
                     PharmacyOrder , MainStorageOrder )

class CitySerializer( serializers.ModelSerializer ) :
    class Meta :
        model = City 
        fields = '__all__' 
        
class LabSerializer( serializers.ModelSerializer ) :
    city = CitySerializer( read_only = True ) 
    class Meta :
        model = Lab 
        fields = '__all__' 
        
class PharmacySerializer( serializers.ModelSerializer ) :
    city = CitySerializer( read_only = True ) 
    class Meta :
        model = Pharmacy 
        fields = '__all__' 
        
class CategorySerializer( serializers.ModelSerializer ) :
    class Meta :
        model = Category
        fields = '__all__' 
        
class ProductSerializer( serializers.ModelSerializer ) :
    category = CategorySerializer( read_only = True )
    lab = LabSerializer( read_only = True ) 
    class Meta :
        model = Product 
        fields = '__all__' 
        
class StorageSerializer( serializers.ModelSerializer ) :
    city = CitySerializer( read_only = True ) 
    class Meta :
        model = Storage
        fields = '__all__' 
        
class MainStorageOfProductsSerializer( serializers.ModelSerializer ) :
    products = ProductSerializer( read_only = True , many = True ) 
    storage = StorageSerializer( read_only = True ) 
    class Meta :
        model = MainStorageOfProducts 
        fields = '__all__' 
        
class PharmacyStorageOfProductsSerializer( serializers.ModelSerializer ) :
    products = ProductSerializer( read_only = True , many = True ) 
    pharmacy = PharmacySerializer( read_only = True ) 
    class Meta :
        model = PharmacyStorageOfProducts 
        fields = '__all__'
        
class PharmacyOrderSerializer( serializers.ModelSerializer ) :
    pharmacy = PharmacySerializer( read_only = True )
    products = ProductSerializer( read_only = True , many = True ) 
    class Meta :
        model = PharmacyOrder 
        fields = '__all__' 
        
class MainStorageOrderSerializer( serializers.ModelSerializer ) :
    storage = MainStorageOfProductsSerializer( read_only = True ) 
    products = ProductSerializer( read_only = True , many = True ) 
    class Meta :
        model = MainStorageOrder 
        fields = '__all__' 
