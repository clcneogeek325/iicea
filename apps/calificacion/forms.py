from django import forms
from .models import calificacion
from apps.alumno.models import alumno


class calificacionForm(forms.ModelForm):
	alumno = forms.ModelChoiceField(queryset=alumno.objects.filter(activo=True))
	class Meta:
		model = calificacion
		exclude = {'activo',}

	
	"""
	def clean_alumno(self):
		a = self.cleaned_dat['alumno']
		c = calificacion.objects.filter(alumno=self.alumno,materia=self.materia,semestre=self.semestre)
		if c.exists():
			print "si existe un"
			raise forms.ValidationError("YA existe un registro con el mismo alumno,materia,semestre")
		return a
	"""
