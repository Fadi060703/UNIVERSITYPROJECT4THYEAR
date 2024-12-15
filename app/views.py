from django.shortcuts import render , get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ( City , Lab , Pharmacy , Category , Product )
from .serializers import ( CitySerializer , LabSerializer , PharmacySerializer , 
                          CategorySerializer , ProductSerializer )
# Create your views here.


class ListCreateCityView( APIView ) :
    serializer_class = CitySerializer 
    
    def get( self , request : Request ) :
        cities = City.objects.all() 
        serializer = self.serializer_class( cities , many = True )
        response = {
            'message' : 'Cities In DB' , 
            'data' : serializer.data
        }
        return Response( data = response , status = status.HTTP_200_OK )
    
    def post( self , request : Request ) :
        city = request.data
        serializer = self.serializer_class( data = city ) 
        if serializer.is_valid() :
            serializer.save()
            response = {
                'message' : 'Added City To DB' ,
                'data' : serializer.data 
            }
            return Response( data = response , status = status.HTTP_201_CREATED ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST )

class RetrieveCityView( APIView ) :
    serializer_class = CitySerializer
    def get( self , request : Request , pk : int ) :
        city = get_object_or_404( City , pk = pk ) 
        serializer = self.serializer_class( city ) 
        response = {
            'message' : 'City Found In DB' ,
            'data' : serializer.data 
        }
        return Response( data = response , status = status.HTTP_200_OK ) 
    
    def put( self , request : Request , pk : int ) :
        city = request.data 
        serializer = self.serializer_class( data = city , pk = pk ) 
        if serializer.is_valid() :
            serializer.save()
            response = {
                'message' : 'City Updataed In DB' ,
                'data' : serializer.data 
            }
            return Response( data = response , status = status.HTTP_201_CREATED ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST ) 

    def patch( self , request : Request , pk : int ) :
        city = request.data 
        serializer = self.serializer_class( data = city , pk = pk , partial = True )  
        if serializer.is_valid() :
            serializer.save()
            response = {
                'message' : 'City Updataed In DB' ,
                'data' : serializer.data 
            }
            return Response( data = response , status = status.HTTP_201_CREATED ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST )
    
    def delete( self , request : Request , pk : int ) :
        city = get_object_or_404( City , pk = pk ) 
        city.delete() 
        return Response( status = status.HTTP_410_GONE )  

class ListCreateLabView( APIView ) :
    serializer_class = LabSerializer
    
    def get( self , request : Request ) :
        labs = Lab.objects.all()
        serializer = self.serializer_class( labs , many = True ) 
        response = {
            'message' : 'Labs In DB' ,
            'data' : serializer.data
        }
        return Response( data = response , status = status.HTTP_200_OK ) 
    
    def post( self , request : Request ) :
        lab = request.data 
        serializer = self.serializer_class( data = lab ) 
        if serializer.is_valid() :
            serializer.save()
            response = {
                'message' : 'Added Lab To DB' ,
                'data' : serializer.data 
            }
            return Response( data = response , status = status.HTTP_201_CREATED )
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST ) 
    
class RetrieveLabView( APIView ) :
    serializer_class = LabSerializer
    
    def get( self , request : Request , pk : int ) :
        lab = get_object_or_404( Lab , pk = pk ) 
        serializer = self.serializer_class( lab ) 
        response = {
            'message' : 'Lab Found In DB' ,
            'data' : serializer.data 
        }
        return Response( data = response , status = status.HTTP_200_OK ) 
    
    def put( self , request : Request , pk : int ) :
        lab = request.data 
        serializer = self.serializer_class( data = lab , pk = pk ) 
        if serializer.is_valid() :
            serializer.save()
            response = {
                'message' : 'Lab Updataed In DB' ,
                'data' : serializer.data 
            }
            return Response( data = response , status = status.HTTP_201_CREATED ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST ) 

    def patch( self , request : Request , pk : int ) :
        lab = request.data 
        serializer = self.serializer_class( data = lab , pk = pk , partial = True )  
        if serializer.is_valid() :
            serializer.save()
            response = {
                'message' : 'Lab Updataed In DB' ,
                'data' : serializer.data 
            }
            return Response( data = response , status = status.HTTP_201_CREATED ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST )
    
    def delete( self , request : Request , pk : int ) :
        lab = get_object_or_404( Lab , pk = pk ) 
        lab.delete() 
        return Response( status = status.HTTP_410_GONE )  
    
class ListCreatePharmacyView( APIView ) :
    serializer_class = PharmacySerializer
    def get( self , request : Request ) :
        pharms = Pharmacy.objects.all()
        serializer = self.serializer_class( pharms , many = True ) 
        response = {
            'message' : 'Pharmacies In DB' ,
            'data' : serializer.data 
        }
        return Response( data = response , status = status.HTTP_200_OK ) 
    
    def post( self , request : Request ) :
        pharm = request.data 
        serializer = self.serializer_class( data = pharm ) 
        if serializer.is_valid() :
            serializer.save()
            response = {
                'message' : 'Pharmacy Added To DB' , 
                'data' : serializer.data 
            }
            return Response( data = response , status = status.HTTP_201_CREATED ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST ) 
        
class RetrievePharmacyView( APIView ) :
    serializer_class = PharmacySerializer
    def get( self , request : Request , pk : int ) :
        pharm = get_object_or_404( Pharmacy , pk = pk )
        serializer = self.serializer_class( pharm ) 
        response = {
            'message' : 'Pharmacy Found In DB' ,
            'data' : serializer.data 
        }
        return Response( data = response , status = status.HTTP_200_OK ) 
    
    def put( self , request : Request , pk : int ) :
        pharm = request.data 
        serializer = self.serializer_class( data = pharm , pk = pk ) 
        if serializer.is_valid() :
            serializer.save()
            response = {
                'message' : 'Pharmacy Updated In DB' , 
                'data' : serializer.data 
            }
            return Response( data = response , status = status.HTTP_201_CREATED ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST )
    
    def patch( self , request : Request , pk : int ) :
        pharm = request.data 
        serializer = self.serializer_class( data = pharm , pk = pk , partial = True ) 
        if serializer.is_valid() :
            serializer.save()
            response = {
                'message' : 'Pharmacy Updated In DB' , 
                'data' : serializer.data 
            }
            return Response( data = response , status = status.HTTP_201_CREATED ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST )
    
    def delete( self , request : Request , pk : int ) :
        pharm = get_object_or_404( Pharmacy , pk = pk ) 
        pharm.delete()
        return Response( status = status.HTTP_410_GONE ) 
    
class ListCreateCategoryView( APIView ) :
    serializer_class = CategorySerializer 
    
    def get( self , request : Request ) :
        categs = Category.objects.all()
        serializer = self.serializer_class( categs , many = True ) 
        response = {
            'message' : 'Categories In DB' , 
            'data' : serializer.data
        }
        return Response( data = response , status = status.HTTP_200_OK ) 
    
    def post( self , request : Request ) :
        categ = request.data 
        serializer = self.serializer_class( data = categ ) 
        if serializer.is_valid() :
            serializer.save()
            response = {
                'message' : 'Category Added To DB' , 
                'data' : serializer.data
            }
            return Response( data = response , status = status.HTTP_201_CREATED ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST ) 
    
class RetrieveCategoryView( APIView ) : 
    serializer_class = CategorySerializer
    
    def get( self , request : Request , pk : int ) :
        categ = get_object_or_404( Category , pk = pk ) 
        serializer = self.serializer_class( categ ) 
        response = {
            'message' : 'Category Found In DB' , 
            'data' : serializer.data
        }
        return Response( data = response , status = status.HTTP_200_OK ) 
    
    def put( self , request : Request , pk : int ) :
        categ = request.data 
        serializer = self.serializer_class( data = categ , pk = pk ) 
        if serializer.is_valid() :
            serializer.save()
            response = {
                'message' : 'Category Updated In DB' , 
                'data' : serializer.data
            }
            return Response( data = response , status = status.HTTP_201_CREATED ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST ) 
    
    def patch( self , request : Request , pk : int ) :
        categ = request.data 
        serializer = self.serializer_class( data = categ , pk = pk , partial = True ) 
        if serializer.is_valid() :
            serializer.save()
            response = {
                'message' : 'Category Updated In DB' , 
                'data' : serializer.data
            }
            return Response( data = response , status = status.HTTP_201_CREATED ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST ) 
    
    def delete( self , request : Request , pk : int ) :
        categ = get_object_or_404( Category , pk = pk ) 
        categ.delete()
        return Response( status = status.HTTP_410_GONE ) 
    
    
class ListCreateProductView( APIView ) :
    serializer_class = ProductSerializer 
    
    def get( self , request : Request ) :
        prod = Product.objects.all()
        serializer = self.serializer_class( prod , many = True ) 
        response = {
            'message' : 'Products In DB' , 
            'data' : serializer.data
        }
        return Response( data = response , status = status.HTTP_200_OK ) 
    
    def post( self , request : Request ) :
        prod = request.data 
        serializer = self.serializer_class( data = prod ) 
        if serializer.is_valid() :
            serializer.save()
            response = {
                'message' : 'Product Added To DB' , 
                'data' : serializer.data
            }
            return Response( data = response , status = status.HTTP_201_CREATED ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST ) 
    
class RetrieveProductView( APIView ) : 
    serializer_class = ProductSerializer
    
    def get( self , request : Request , pk : int ) :
        prod = get_object_or_404( Product , pk = pk ) 
        serializer = self.serializer_class( prod ) 
        response = {
            'message' : 'Product Found In DB' , 
            'data' : serializer.data
        }
        return Response( data = response , status = status.HTTP_200_OK ) 
    
    def put( self , request : Request , pk : int ) :
        prod = request.data 
        serializer = self.serializer_class( data = prod , pk = pk ) 
        if serializer.is_valid() :
            serializer.save()
            response = {
                'message' : 'Product Updated In DB' , 
                'data' : serializer.data
            }
            return Response( data = response , status = status.HTTP_201_CREATED ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST ) 
    
    def patch( self , request : Request , pk : int ) :
        prod = request.data 
        serializer = self.serializer_class( data = prod , pk = pk , partial = True ) 
        if serializer.is_valid() :
            serializer.save()
            response = {
                'message' : 'Product Updated In DB' , 
                'data' : serializer.data
            }
            return Response( data = response , status = status.HTTP_201_CREATED ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST ) 
    
    def delete( self , request : Request , pk : int ) :
        prod = get_object_or_404( Product , pk = pk ) 
        prod.delete()
        return Response( status = status.HTTP_410_GONE ) 