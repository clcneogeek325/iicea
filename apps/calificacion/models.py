from django.db import models
from django.contrib.auth.models import User
from apps.alumno.models import alumno
from apps.materia.models import materia
from apps.semestre.models import semestre


class calificacion(models.Model):
	alumno = models.ForeignKey(alumno,null=False)
	materia = models.ForeignKey(materia,null=False)
	calificacion = models.FloatField()
	activo = models.BooleanField(default=True)
	semestre = models.ForeignKey(semestre,null=False)
	def __unicode__(self):
		return self.alumno.alumno.first_name
