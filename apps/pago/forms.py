from django import forms
from .models import pago
from apps.alumno.models import alumno


class pagoForm(forms.ModelForm):
	alumno = forms.ModelChoiceField(queryset=alumno.objects.filter(activo=True),label="Alumnos")
	class Meta:
		model = pago
		fields = '__all__'
		
