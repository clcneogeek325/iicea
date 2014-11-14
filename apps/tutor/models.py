from django.db import models


class tutor(models.Model):
	nombre = models.CharField(max_length=30,null=False)
	apellidos = models.CharField(max_length=30,null=True)
	parentesco = models.CharField(max_length=30,null=True)
	ocupacion = models.CharField(max_length=30,null=True)
	activo = models.BooleanField(default=True)
	def __unicode__(self):
		return self.nombre

