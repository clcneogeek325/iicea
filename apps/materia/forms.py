from django import forms
from .models import materia
from django.forms import Textarea

class materiaForm(forms.ModelForm):
	class Meta:
		model = materia
		fields = ['nombre','semestre','semanas','actividades']
		widgets = {
		'actividades': Textarea(attrs={'cols': 80, 'rows': 20}),
		}
