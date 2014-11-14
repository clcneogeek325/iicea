from django.db import models
from django.contrib.auth.models import User
from apps.alumno.models import alumno
from apps.materia.models import materia

class calificacion(models.Model):
	alumno = models.ForeignKey(alumno,null=False)
	materia = models.ForeignKey(materia,null=False)
	calificacion = models.FloatField()
	def __unicode__(self):
		return self.alumno.first_name
