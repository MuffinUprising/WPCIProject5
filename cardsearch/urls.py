__author__ = 'casey'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.card_list, name='card_list'),
    url(r'^card/(?P<pk>\d+)/$', views.card_detail, name='card_detail'),
]