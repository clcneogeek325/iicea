from django import forms
from .models import alumno
from apps.materia.models import materia
from apps.tutor.models import tutor
from apps.grupo.models import grupo
from apps.semestre.models import semestre
from apps.horario.models import horario

class nombreYpellidoForm(forms.Form):
	nombre = forms.CharField()
	apellidos = forms.CharField()

class alumnoForm(forms.ModelForm):
	tutor = forms.ModelChoiceField(queryset=tutor.objects.filter(activo=True))
	grupo = forms.ModelChoiceField(queryset=grupo.objects.filter(activo=True))
	materias = forms.ModelMultipleChoiceField(queryset=materia.objects.filter(activo=True))
	semestre = forms.ModelMultipleChoiceField(queryset=semestre.objects.filter(activo=True))
	horario = forms.ModelChoiceField(queryset=horario.objects.filter(activo=True))
	class Meta:
		model = alumno
		exclude = {'alumno','activo'}
		
