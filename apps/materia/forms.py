from django import forms
from .models import materia

class materiaForm(forms.ModelForm):
	class Meta:
		model = materia
		exclude = {'activo',}
		
