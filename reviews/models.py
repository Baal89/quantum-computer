from django.db import models
from django.utils import timezone
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete = models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    
    def __unicode__(self):
        return self.title
        