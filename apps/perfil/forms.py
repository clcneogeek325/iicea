from django import forms
from .models import perfil

class perfilForm(forms.ModelForm):
	class Meta:
		model = perfil
		exclude  = {'activo',}
