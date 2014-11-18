from django.db import models
from apps.empleado.models import empleado
from apps.horario.models import horario

class asistencia_empleado(models.Model):
	empleados = models.ManyToManyField(empleado,blank=False,null=False)
	horario = models.ForeignKey(horario)
	fecha = models.DateField(blank=False, null=False)
	activo = models.BooleanField(default=True)
	def __unicode__(self):
		str_fecha= str(self.fecha)
		return str_fecha


