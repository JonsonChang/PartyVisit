# coding=UTF-8

from django import forms
from django.forms import ModelForm

from .models import *

class NameForm(forms.Form):
    your_namea = forms.CharField(label='名稱', max_length=100)

#=================================	
class addressForm(ModelForm):
    class Meta:
        model = address
        fields = '__all__'
	
class historyForm(ModelForm):
    class Meta:
        model = history
        fields = '__all__'
		
class peopleForm(ModelForm):
    class Meta:
        model = people
        fields = '__all__'		