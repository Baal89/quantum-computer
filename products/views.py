from django.views.generic.list import ListView
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product
from checkout.models import OrderLineItem
from reviews.models import Review

def get_product(request, id):
    """
    A view that return the selected product
    """
    product = Product.objects.get(id=id)
    reviews = Review.objects.filter(product=product).order_by('-create_date')
    
    reviews_total = 0
    reviews_count = 0
    if reviews:
        for review in reviews:
            reviews_total += review.rating
            reviews_count += 1
            
        average_rating = round((reviews_total / reviews_count) * 2) /2
            
    else:
        average_rating = 0
    
    args = {'product': product, 'reviews': reviews, 'average_rating': average_rating}
    return render(request, 'get_product.html', args, round(average_rating * 2) / 2)
    
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