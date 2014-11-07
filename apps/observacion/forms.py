from django import forms
from .models import observacion

class observacionForm(forms.ModelForm):
	class Meta:
		model = observacion
		fields = '__all__'
		
