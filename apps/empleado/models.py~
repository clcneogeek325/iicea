from django.db import models
from django.contrib.auth.models import User
from apps.perfil.models import perfil

class empleado(models.Model):
	empleado = models.ForeignKey(User,null=False)
	localidad = models.CharField(max_length=30,null=True)
	municipio = models.CharField(max_length=30,null=True)
	telefono = models.CharField(max_length=30,null=True)
	sexo = models.CharField(max_length=30,null=True)
	perfil = models.ForeignKey(perfil,null=True)
	activo = models.BooleanField(default=True)
	def __unicode__(self):
		return self.empleado.first_name

	

