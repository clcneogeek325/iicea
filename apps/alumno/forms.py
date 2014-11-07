from django import forms
from .models import alumno

class alumnoForm(forms.ModelForm):
	nombre = forms.CharField()
	apellidos = forms.CharField()
	class Meta:
		model = alumno
		exclude = {'alumno'}
		
