from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Review
from .forms import ReviewForm
from products.models import Product
from products.views import get_product

def create_review(request, id):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    
    product = Product.objects.get(id=id)
    
    if request.method == "POST":
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            form.save()
                
            return redirect(get_product,  product.id)
    else:
        form = ReviewForm()
    return render(request, 'reviewform.html', {'form': form})
    











