from django.conf.urls import url
from django.contrib import admin
from . import views


    
    
urlpatterns = [
   url(r'^$', views.home, name='home'),
   url(r'^documentation/', views.about, name='about'),
   url(r'^support/', views.contact, name='contact'),

    
]