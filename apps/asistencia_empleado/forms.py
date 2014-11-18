from django import forms
from .models import asistencia_empleado
from apps.empleado.models import empleado

class asistencia_empleadoForm(forms.ModelForm):
	empleados = forms.ModelMultipleChoiceField(queryset=empleado.objects.filter(activo=True),label="Docente")
	class Meta:
		model = asistencia_empleado
		exclude = {'activo',}
		
