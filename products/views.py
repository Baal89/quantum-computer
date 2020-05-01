from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Product

def get_product(request, id):
    """
    A view that return the selected product
    """
    product = Product.objects.get(id=id)
    
    args = {'product': product}
    return render(request, 'get_product.html', args)
    
def category(request, type):
    """
    A view that return the specified category
    """
    products = Product.objects.filter(product_type=type)
    args = {'products': products}
    return render(request, 'category.html', args)