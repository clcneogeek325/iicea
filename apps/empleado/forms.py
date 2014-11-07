from django import forms
from .models import empleado
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class empleadoForm(forms.ModelForm):
	nombre = forms.CharField()
	apellidos = forms.CharField()
	class Meta:
		model = empleado
		exclude = {'empleado'}


