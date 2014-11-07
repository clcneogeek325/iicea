from django import forms
from .models import nomina

class nominaForm(forms.ModelForm):
	class Meta:
		model = nomina
		fields = '__all__'
		
