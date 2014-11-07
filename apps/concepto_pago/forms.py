from django import forms
from .models import concepto_pago

class concepto_pagoForm(forms.ModelForm):
	class Meta:
		model = concepto_pago
		fields = '__all__'
		
