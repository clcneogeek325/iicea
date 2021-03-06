from django import forms
from .models import observacion
from apps.alumno.models import alumno


class observacionForm(forms.ModelForm):
	alumno = forms.ModelChoiceField(queryset=alumno.objects.filter(activo=True),label="Alumno")
	class Meta:
		model = observacion
		exclude = {'activo',}
		
