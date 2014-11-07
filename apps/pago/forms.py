from django import forms
from .models import pago

class pagoForm(forms.ModelForm):
	class Meta:
		model = pago
		fields = '__all__'
		
