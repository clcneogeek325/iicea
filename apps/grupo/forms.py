from django import forms
from .models import grupo

class grupoForm(forms.ModelForm):
	class Meta:
		model = grupo
		fields = '__all__'
		
