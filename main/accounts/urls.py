from django import views
from django.urls import path
from django.http  import HttpResponse
from . import views

app_name ='home'


urlpatterns = [
    path('' , views.home , name= 'home') , 
    path('api/' , views.url , name='url')
]