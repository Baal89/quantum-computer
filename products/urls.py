from django.conf.urls import url
from .views import get_product, category

urlpatterns = [
    url(r'get_product/(?P<id>\d+)', get_product, name="get_product"),
    url(r'category/(?P<type>[-\w]+)$', category, name="category")
]