from django.conf.urls import url
from .views import all_product, get_product, amd_processors

urlpatterns = [
    url(r'all_product/', all_product, name="products"),
    url(r'get_product/(?P<id>\d+)', get_product, name="get_product"),
    url(r'amd_processors/', amd_processors.as_view(), name="amd-list")
]