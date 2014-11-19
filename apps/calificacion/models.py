from django.db import models
from django.contrib.auth.models import User
from apps.alumno.models import alumno
from apps.materia.models import materia
from apps.semestre.models import semestre


class calificacion(models.Model):
	alumno = models.ForeignKey(alumno,null=False,blank=False)
	materia = models.ForeignKey(materia,null=False,blank=False)
	calificacion = models.FloatField(null=False,blank=False)
	activo = models.BooleanField(default=True)
	semestre = models.ForeignKey(semestre,null=False,blank=False)
	def __unicode__(self):
		return self.alumno.alumno.first_name
