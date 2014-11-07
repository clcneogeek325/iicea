from django import forms
from .models import horario

class horarioForm(forms.ModelForm):
	class Meta:
		model = horario
		fields = '__all__'
		
