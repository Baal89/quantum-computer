from django.db import models
from django.utils import timezone
from products.models import Product
from django.contrib.auth.models import User


# Create your models here.
class Review(models.Model):
    RATING_CHOICE = (
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
)

    product = models.ForeignKey(Product, null=True, on_delete = models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=RATING_CHOICE)
    
    def __unicode__(self):
        return self.title
    
    