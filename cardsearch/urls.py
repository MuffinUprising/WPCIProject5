__author__ = 'casey'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^card/(?P<pk>\d+)/$', views.card_detail, name='card_detail'),
    url(r'^search/$', views.card_list, name='card_list'),
]