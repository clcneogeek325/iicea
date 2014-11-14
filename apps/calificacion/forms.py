from django import forms
from .models import calificacion

class calificacionForm(forms.ModelForm):
	class Meta:
		model = calificacion
		exclude = {'__all__'}
		
