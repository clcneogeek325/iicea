from django import forms
from .models import asistencia_alumno
from apps.alumno.models import alumno
from apps.empleado.models import empleado

class asistencia_alumnoForm(forms.ModelForm):
	empleado = forms.ModelChoiceField(queryset=empleado.objects.filter(activo=True),label="Docente")
	alumnos = forms.ModelMultipleChoiceField(queryset=alumno.objects.filter(activo=True),label="Alumnos")
	class Meta:
		model = asistencia_alumno
		exclude = {'activo',}
		
