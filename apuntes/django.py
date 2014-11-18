	def __init__(self, *args, **kwargs):
		super(alumnoForm, self).__init__(*args, **kwargs)
		self.fields['tutor'].queryset = tutor.objects.filter(activo=True)
		self.fields['grupo'].queryset = grupo.objects.filter(activo=True)
		self.fields['materias'].queryset = materia.objects.filter(activo=True)
		self.fields['semestre'].queryset = semestre.objects.filter(activo=True)
