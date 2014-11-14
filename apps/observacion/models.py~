from django.db import models
from django.contrib.auth.models import User
from apps.alumno.models import alumno

class observacion(models.Model):
	observacion = models.CharField(max_length=50,null=False)
	alumno = models.ForeignKey(alumno,null=False)
	def __unicode__(self):
		return self.alumno.alumno.username
