from django.conf.urls import url
from .views import get_review, create_or_edit

urlpatterns = [
    url(r'^$', get_review, name="get_review"),
    url(r'^new/$', create_or_edit, name='new_review'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit, name="edit_post")
]