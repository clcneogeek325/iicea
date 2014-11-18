from django import forms
from .models import nomina
from apps.empleado.models import empleado

class nominaForm(forms.ModelForm):
	empleado = forms.ModelChoiceField(queryset=empleado.objects.filter(activo=True))
	class Meta:
		model = nomina
		exclude = {'activo',}
		
