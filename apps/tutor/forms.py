from django import forms
from .models import tutor

class tutorForm(forms.ModelForm):
	class Meta:
		model = tutor
		exclude = {'activo',}
		
