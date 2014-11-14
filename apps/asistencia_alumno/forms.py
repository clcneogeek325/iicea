from django import forms
from .models import asistencia_alumno
from apps.alumno.models import alumno

class asistencia_alumnoForm(forms.ModelForm):
	empleado = forms.ModelMultipleChoiceField(queryset=alumno.objects.filter(activo=True),label="Docente")
	alumnos = forms.ModelMultipleChoiceField(queryset=alumno.objects.filter(activo=True),label="Alumnos")
	class Meta:
		model = asistencia_alumno
		fields = '__all__'
		
