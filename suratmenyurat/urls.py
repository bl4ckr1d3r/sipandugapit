from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^delete/(?P<delete_id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^print/(?P<sku_id>[0-9]+)/$', views.print, name='print'),
    url(r'^create/$', views.create, name='create'),
    url(r'^$', views.list, name='list'),
]