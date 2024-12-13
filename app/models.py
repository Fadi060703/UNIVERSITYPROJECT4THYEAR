from django.db import models 

class City( models.Model ) :
    name = models.CharField( max_length = 20 , null = False , blank = False , unique = True )
    
    def __str__( self ) :
        return self.name 
    
    
class Lab( models.Model ) :
    name = models.CharField( max_length = 50 , null = False , blank = False , unique = True ) 
    location = models.ForeignKey( City , on_delete = models.CASCADE , related_name = 'LabInCity' ) 
    is_active = models.BooleanField( default = True )
    
    def __str__( self ) :
        return self.name 
    
class Pharmacy( models.Model ) :
    name = models.CharField( max_length = 50 , null = False , blank = False , unique = True ) 
    owner = models.CharField( max_length = 50 , null = False , blank = False )
    city = models.ForeignKey( City , on_delete = models.CASCADE , related_name = 'PharmInCity' ) 
    phone_number = models.CharField( max_length = 10 , null = False , blank = False , unique = True ) 
    email = models.EmailField() 
    
    def __str__( self ) :
        return self.name 
    
class Category( models.Model ) :
    name = models.CharField( max_length = 50 , null = True , blank = True , unique = True ) 
    description = models.TextField( null = True , blank = True ) 
    
    def __str__( self ) :
        return self.name 
    
class Product( models.Model ) :
    name = models.CharField( max_length = 50 , null = False , blank = False ) 
    type = models.CharField( max_length = 50 , null = False , blank = False ) 
    dose = models.DecimalField( max_digits = 10 , decimal_places = 3 , null = True , blank = True )
    category = models.ForeignKey( Category , on_delete = models.CASCADE , related_name = 'ProdCat' ) 
    lab = models.ForeignKey( Lab , on_delete = models.CASCADE , related_name = 'ProdLab' )
    description = models.TextField( null = True , blank = True ) 
    needs_perscription = models.BooleanField( default = False ) 
    prod_date = models.DateField()
    exp_date = models.DateField()
    
    def __str__( self ) :
        return self.name 
    
    def clean( self ) :
        from django.core.exceptions import ValidationError 
        if self.exp_date <= self.prod_date :
            raise ValidationError( '' )

class Storage( models.Model ) :
    name = models.CharField( max_length = 50 , null = False , blank = True ) 
    city = models.ForeignKey( City , on_delete = models.CASCADE , related_name = 'StorageInCity' ) 
    
    def __str__( self ) :
        return self.name 
    
class MainStorageOfProducts( models.Model ) :
    product = models.ForeignKey( Product , on_delete = models.CASCADE , related_name = 'ProdMainStorage' ) 
    storage = models.ForeignKey( Storage , on_delete = models.CASCADE , related_name = 'Storage' ) 
    quantity = models.PositiveIntegerField( default = 0 ) 
    
    class Meta :
        unique_together = ( 'product' , 'storage' ) 
    
class PharmacyStorageOfProducts( models.Model ) :
    product = models.ForeignKey( Product , on_delete = models.CASCADE , related_name = 'ProdPharmStorage' ) 
    pharmacy = models.ForeignKey( Pharmacy , on_delete = models.CASCADE , related_name = 'Pharm' ) 
    quantity = models.PositiveIntegerField( default = 0 ) 
    
    class Meta :
        unique_together = ( 'product' , 'pharmacy' ) 
        
class PharmacyOrder( models.Model ) :
    pharmacy = models.ForeignKey( Pharmacy , on_delete = models.CASCADE , related_name = 'OrderPharm' )
    product = models.ForeignKey( Product , on_delete = models.CASCADE , related_name = 'OrderProd' )
    quantity = models.PositiveIntegerField( default = 1 ) 
    order_date = models.DateTimeField( auto_now_add = True )
    
    class Meta :
        unique_together = ( 'pharmacy' , 'product' , 'order_date' ) 
        
    def check_order( self ) :
        main_storage = MainStorageOfProducts.objects.get( product = self.product ) 
        if main_storage.quantity >= self.quantity :
            main_storage.quantity -= self.quantity 
            main_storage.save()
            self.save()
        else :
            raise ValueError( '' )  
        
