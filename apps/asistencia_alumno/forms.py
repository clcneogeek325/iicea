from django import forms
from .models import asistencia_alumno

class asistencia_alumnoForm(forms.ModelForm):
	class Meta:
		model = asistencia_alumno
		fields = '__all__'
		
