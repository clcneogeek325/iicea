from django import forms
from .models import asistencia_empleado

class asistencia_empleadoForm(forms.ModelForm):
	class Meta:
		model = asistencia_empleado
		fields = '__all__'
		
