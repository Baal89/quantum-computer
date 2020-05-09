from django.views.generic.list import ListView
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    A view that return the specified category of products
    and implement a pagination system for the pages.
    """
    products = Product.objects.filter(product_type=type)
    page = request.GET.get('page', 1)
    
    paginator = Paginator(products, 6)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    args = {'products': products}
    return render(request, 'category.html', args)