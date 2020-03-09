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
    
class amd_processors(ListView):
    template_name = 'amd_processors.html'
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super(amd_processors, self).get_context_data(**kwargs)
        context['product_type'] = 'AMD_CPU'
        return context