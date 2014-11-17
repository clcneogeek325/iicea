from django import forms
from .models import alumno
from apps.materia.models import materia
from apps.tutor.models import tutor
from apps.grupo.models import grupo
from apps.semestre.models import semestre


class nombreYpellidoForm(forms.Form):
	nombre = forms.CharField()
	apellidos = forms.CharField()

class alumnoForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(alumnoForm, self).__init__(*args, **kwargs)
		self.fields['tutor'].queryset = tutor.objects.filter(activo=True)
		self.fields['grupo'].queryset = grupo.objects.filter(activo=True)
		self.fields['materias'].queryset = materia.objects.filter(activo=True)
		self.fields['semestre'].queryset = semestre.objects.filter(activo=True)
	class Meta:
		model = alumno
		exclude = {'alumno','activo'}
		
