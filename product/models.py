from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=254, default='product name')
    description = models.TextField()
    feature = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    size = models.CharField(max_length=254, blank=True)
    
    
    #specific attributes
    
    def __str__(self):
        return self.name
        
