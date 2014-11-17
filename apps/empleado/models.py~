from django.db import models
from django.contrib.auth.models import User
from apps.perfil.models import perfil

class empleado(models.Model):
	TIPO_SEXO = (
	('Hombre', 'Hombre'),
	('Mujer', 'Mujer'),
	)

	empleado = models.ForeignKey(User,null=False)
	localidad = models.CharField(max_length=30,null=True,blank=True)
	municipio = models.CharField(max_length=30,null=True,blank=True)
	telefono = models.CharField(max_length=30,null=True,blank=True)
	sexo = models.CharField(max_length=100,choices=TIPO_SEXO)
	perfil = models.ForeignKey(perfil,null=True,blank=True)
	activo = models.BooleanField(default=True)
	def __unicode__(self):
		return self.empleado.first_name

	

