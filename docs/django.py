from django.db import models
from apps.semestre.models import semestre

class materia(models.Model):
	nombre = models.CharField(max_length=30,null=False,blank=False)
	semestre = models.ForeignKey(semestre,null=False,blank=False)
	semanas = models.IntegerField(max_length=10,null=False,blank=False)
	actividades = models.CharField(max_length=200,null=False,blank=False)
	activo = models.BooleanField(default=True)
	def __unicode__(self):
		return self.nombre


