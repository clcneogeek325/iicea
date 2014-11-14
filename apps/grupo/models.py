from django.db import models


class grupo(models.Model):
	nombre = models.CharField(max_length=30,null=False)
	activo = models.BooleanField(default=True)
	def __unicode__(self):
		return self.nombre

