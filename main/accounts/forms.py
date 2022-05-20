from dataclasses import field
from django import forms
from . import models


class urlform(forms.ModelForm):
    class Meta: 
        model = models.urls
        fields = ('__all__')



class loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField()