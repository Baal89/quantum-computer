from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Product

# Create your views here.
def all_product(request):
    """
    A view that return all the products in products.html
    """
    products = Product.objects.all()
    
    args = {'products': products}
    return render(request, 'products.html', args)
    
def get_product(request, id):
    """
    A view that return the selected product
    """
    product = Product.objects.get(id=id)
    
    args = {'product': product}
    return render(request, 'get_product.html', args)
    
def category(request):
    """
    A view that return the specified category
    """
    products = Product.objects.get('AMD_CPU')
    args = {'products': products}
    return render(request, 'category.html', args)