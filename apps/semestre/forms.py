from django import forms
from .models import semestre

class semestreForm(forms.ModelForm):
	class Meta:
		model = semestre
		fields = '__all__'
