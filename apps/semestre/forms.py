from django import forms
from .models import semestre

class semestreForm(forms.ModelForm):
	class Meta:
		model = semestre
		exclude = {'activo',}
