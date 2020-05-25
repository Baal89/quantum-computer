from django.conf.urls import url
from .views import create_review

urlpatterns = [
    url(r'^create_review/(?P<id>\d+)$', create_review, name='new_review'),
]