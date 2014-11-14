from django import forms
from .models import calificacion
from apps.alumno.models import alumno


class calificacionForm(forms.ModelForm):
	alumno = forms.ModelChoiceField(queryset=alumno.objects.filter(activo=True))
	class Meta:
		model = calificacion
		fields = ('__all__')
		
