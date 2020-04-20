from django import forms
from .models import *

class FarhanForm(forms.ModelForm):
	class Meta:
		model = Farhan
		fields = ('Image', 'Date', 'FY', 'Title', 'Price', 'Category', 'Capital')


class NadiaForm(forms.ModelForm):
	class Meta:
		model = Nadia
		fields = ('Image', 'Date', 'FY', 'Title', 'Price', 'Category','Capital')


class FarhanFamilyForm(forms.ModelForm):
	class Meta:
		model = FarhanFamily
		fields = ('Image', 'Date', 'FY', 'Title', 'Price', 'Category','Capital')


class OngieForm(forms.ModelForm):
	class Meta:
		model = Ongie
		fields = ('Image', 'Date', 'FY', 'Title', 'Price', 'Category','Capital')


class OrangeForm(forms.ModelForm):
	class Meta:
		model = Orange
		fields = ('Image', 'Date', 'FY', 'Title', 'Price', 'Category','Capital')