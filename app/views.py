from django.shortcuts import render
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ( City , Lab )
from .serializers import ( CitySerializer , LabSerializer )
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
    