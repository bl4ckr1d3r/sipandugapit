from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^delete/(?P<delete_id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^update/(?P<update_id>[0-9]+)/$', views.update, name='update'),
    url(r'^create/$', views.create, name='create'),
    url(r'^$', views.list, name='list'),
    url(r'^anggotakeluargalist/', views.anggotakeluargalist, name='anggotakeluargalist'),
    url(r'^anggotakeluargacreate/', views.anggotakeluargacreate, name='anggotakeluargacreate'),
    url(r'^anggotakeluargadelete/(?P<delete_id>[0-9]+)/$', views.anggotakeluargadelete, name='anggotakeluargadelete'),
]