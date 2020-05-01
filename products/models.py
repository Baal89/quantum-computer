from django.db import models

# Create your models here.

class Product(models.Model):
    TYPE_AMD_CPU = 'AMD_CPU'
    TYPE_INTEL_CPU = 'Intel_CPU'
    TYPE_AMD_CARD = 'AMD_graphic_cards'
    TYPE_NVIDIA_CARD = 'Nvidia_graphic_cards'
    TYPE_MOTHERBOARD = 'Motherboard'
    TYPE_STORAGE = 'Storage'
    TYPE_CHOICES = (
        (TYPE_AMD_CPU, 'AMD CPU'),
        (TYPE_INTEL_CPU, 'Intel CPU'),
        (TYPE_AMD_CARD, 'AMD graphic cards'),
        (TYPE_NVIDIA_CARD, 'Nvidia graphic cards'),
        (TYPE_MOTHERBOARD, 'Motherboard'),
        (TYPE_STORAGE, 'Storage'),
    )
    
    product_type = models.CharField(max_length=30, choices=TYPE_CHOICES, blank=False, default='product type')
    
    name = models.CharField(max_length=254, default='product name')
    description = models.TextField()
    feature = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    
    
    #specific attributes
    
    def __str__(self):
        return self.name
        
