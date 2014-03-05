from django import forms
from portal.models import *
from django.contrib.admin import widgets

class AddEventForm(forms.ModelForm):
	#name = forms.CharField(max_length=30)
	#description = forms.CharField(max_length=60,widget=forms.Textarea)
	#date_time = forms.DateTimeField('date_time')
	#location = forms.CharField(max_length=40)
	
	class Meta:
		model = Event
		exclude = ('users', )

class AddUpdateForm(forms.ModelForm):
	
	class Meta:
		model = Update
		
class HomepageForm(forms.ModelForm):
	
	class Meta:
		model = Homepage