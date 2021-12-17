from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='login'),
    url(r'^logout/$', views.logoutview, name="logout")
] 
