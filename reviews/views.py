from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Review
from .forms import ReviewForm

# Create your views here.
def get_review(request):
    """
    Create a view that will return a list 
    of Review that were pubblished prior to 'now'
    and render them to the get_product.html
    """
    reviews = Review.objects.filter(create_date=timezone.now()
        ).order_by('create_date')
    return render(request, "get_product.html", {'reviews': reviews})

def create_or_edit(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    reviews = get_object_or_404(Review, pk=pk) if pk else None
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=reviews)
        if form.is_valid():
            reviews = form.save()
            return redirect('profile')
    else:
        form = ReviewForm(instance=reviews)
    return render(request, 'reviewform.html', {'form': form})