from django.db import models
from django.contrib.auth.models import User


class observacion(models.Model):
	observacion = models.CharField(max_length=50,null=False)
	alumno = models.ForeignKey(User,null=True)
	def __unicode__(self):
		return self.alumno.last_name
