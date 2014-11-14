from django.db import models
from apps.empleado.models import empleado

class asistencia_empleado(models.Model):
	empleados = models.ManyToManyField(empleado,blank=False,null=False)
	hora_entrada = models.TimeField(blank=False, null=False)
	hora_salida = models.TimeField(blank=False, null=False)
	fecha = models.DateField(blank=False, null=False)
	activo = models.BooleanField(default=True)
	def __unicode__(self):
		str_fecha= str(self.fecha)
		return str_fecha


