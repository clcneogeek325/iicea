from django.db import models
from django.contrib.auth.models import User


class alumno(models.Model):
	alumno = models.OneToOneField(User,null=False)
	sexo = models.CharField(max_length=20,null=True)
	curp = models.CharField(max_length=20,null=True)
	fecha_nacimiento = models.DateField(null=True)
	localidad = models.CharField(max_length=30,null=True)
	municipio = models.CharField(max_length=30,null=True)
	email = models.CharField(max_length=30,null=True)
	dia = models.CharField(max_length=20,null=True)
	telefono = models.CharField(max_length=20,null=True)
	def __unicode__(self):
		return self.alumno.first_name
