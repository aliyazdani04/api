from curses import pair_content
import re
from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import forms
from django.contrib.auth import login , authenticate , logout
# Create your views here.

def home(request):
    if request.method == 'POST' :
        urlform = forms.urlform(request.POST)
        
        if urlform.is_valid():
            data = urlform.cleaned_data
            models.urls.objects.create(url=data['url'])


       
    else:
        logform = forms.loginform()
        urlform = forms.urlform()
    return render(request  , 'home.html' , { 'url' :urlform})


def url(request):
    data = models.urls.objects.all()
    return render(request  , 'api.html' , context={'data' : data})
        