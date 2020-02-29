from django.shortcuts import render

# Create your views here.

def index(request):
    """
    A view that render index.html
    """
    return render(request, 'index.html')