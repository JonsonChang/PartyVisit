# coding=UTF-8

from django import forms
from django.forms import ModelForm

from .models import *

#=================================	
class addressForm(ModelForm):
    class Meta:
        model = address
        fields = '__all__'
#        fields = ['pub_date', 'headline', 'content', 'reporter']
	
class historyForm(ModelForm):
    class Meta:
        model = history
        fields = '__all__'
		
class peopleForm(ModelForm):
    class Meta:
        model = people
        fields = '__all__'	
        exclude = ['is_del', 'auth', 'password', 'address']